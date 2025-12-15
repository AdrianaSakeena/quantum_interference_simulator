# Quantum Interference Simulator (Baseline)

This project builds a classical foundation for a quantum interference simulator.
It begins by modeling particle detection on a finite-resolution screen using
classical probability laws, and then extends the same experimental setup to
demonstrate how quantum superposition produces interference patterns.

The goal is to isolate exactly which classical assumptions fail and why
quantum mechanics is required.

## Experiment 1: Single Slit Measurement (Classical Prediction)
- Particles are sampled from a Gaussian distribution, representing the angular spread of particles emerging from a single slit.
- The detector has finite spatial resolution.
- The probability density on the screen is reconstructed via a histogram of particle impacts.

This baseline experiment is used to validate the detector model and classical
sampling approach before introducing two slits, quantum superposition,
and interference effects.

## Experiment 2: The Double Slit Measurement (Classical Prediction)
An electron gun emits electrons toward a barrier containing two narrow slits.
After passing through the slits, the electrons travel onward and strike a
detection screen positioned behind the barrier. The detector records the
position at which each electron arrives on the screen.

Under classical physics, electrons are treated as particles that travel as
discrete, localized packets. Each electron passes through one slit only and
does not interact with or influence other electrons. As a result, classical
physics predicts that the pattern observed on the detection screen arises
solely from the accumulation of individual particle impacts governed by
classical probability laws.

Classical physics therefore predicts that the resulting distribution on the 
detection screen is the sum of two independent single-slit distributions, 
producing two smooth peaks with no interference fringes.

Classical Double-Slit Assumptions:
- Each particle passes through one slit only. 
- Particles do not influence each other. 
- Each slit produces a smooth probability distribution on the screen. 
- The probability density from each slit is highest at the position aligned with that slit.
- The two slits are identical, so particles have an equal probability of passing through either slit. 
- The detector records only the position of arrival, not which slit the particle passed through. 
- No phase or interference effects are included in this model. 

 

Results:
<img width="472" height="359" alt="image" src="https://github.com/user-attachments/assets/ff839abc-fdae-457a-a392-7d8d8d2b8a96" />

The classical double-slit experiment produces a probability distribution consisting of two smooth Gaussian peaks, each corresponding to one of the slits. The peaks are centered at positions aligned with the slit locations, and their similar heights indicate an equal probability for particles to pass through either slit. The continuous, non-oscillatory shape of the distribution reflects the statistical independence of particle arrivals and the absence of any interference effects. Consistent with classical mechanics, the observed pattern is simply the sum of two independent single-slit distributions and exhibits no interference fringes.This result establishes a classical baseline and highlights the inability of classical probability theory to produce interference patterns.


## Experiment 3: Double-Slit Measurement (Observed Result, No Path Detection)

When the double-slit experiment is performed without any measurement determining which slit an electron passes through, the resulting distribution on the detection screen exhibits an interference pattern rather than the smooth, additive distributions predicted by classical probability theory. This behavior cannot be explained by treating electrons as classical particles following definite trajectories.

Instead, experimental results are consistent with a quantum description in which electrons are represented by complex probability amplitudes. These amplitudes propagate through both slits coherently, carry phase information, and interfere when combined. Regions of constructive and destructive interference emerge naturally from this superposition.

<img width="318" height="159" alt="image" src="https://github.com/user-attachments/assets/f727cde7-17c3-4f91-8be4-e07f40c579a4" />

In this experiment, we model the observed double-slit interference pattern by replacing classical probability addition with quantum amplitude superposition, demonstrating how interference arises as a purely quantum effect.

Modeling Assumptions:
This simulation makes the following controlled assumptions in order to isolate quantum interference effects:
- One-dimensional screen coordinate
- Idealized, coherent slits
- No environmental decoherence
- No which-path detector or measurement
- Particle feels no external force
- Narrow-slit (point-source) approximation

These assumptions are not meant to fully replicate a real laboratory experiment, but rather to model the essential quantum mechanism responsible for interference.

Note on Slit Modeling:
Each slit is modeled as a coherent source whose contributions are summed at the level of complex probability amplitudes.

Discretely sampling or randomly selecting individual entry points within a slit would introduce implicit which-path information and suppress interference, effectively reducing the model to a classical mixture. For this reason, all possible paths through a slit are treated as simultaneously contributing to the complex probability amplitude at each screen position.

A more detailed model incorporating finite slit width would require integrating amplitudes over all possible entry points within the slit.

results:
 (picture here)



1. Determining the Geometry of Particle Path:
   
- What path does the particle take?
  
The first step in the model is to determine the geometric path length from a slit to a point on the screen.

The slit plane is separated from the screen by a fixed horizontal distance L. A point on the screen is located at vertical position x, while slit 1 is located at vertical position y₁. The vertical separation between the slit and the screen point is therefore x − y₁.

These distances form the legs of a right triangle, whose hypotenuse corresponds to the total distance traveled by the particle. Using the Pythagorean theorem, the path length from slit 1 to screen position x is

r₁(x) = √(L² + (x − y₁)²).

Although the slit-to-screen distance L is constant, the vertical separation x − y₁ varies across the screen. As a result, each screen position corresponds to a unique path length. These geometric path lengths form the foundation for determining the quantum phase accumulated along each path.






2. Determining the Phase Accumulated Along a Path:
   
In quantum mechanics, phase is proportional to distance traveled. While phase is not directly observable, it plays a crucial role in determining how probability amplitudes interfere when combined.

For a particle with wavelength λ, the phase accumulated over a distance r is given by

phase = k r,
where k = 2π / λ.

The quantity k determines how rapidly the phase rotates in space, while r specifies how far along this rotation the particle has traveled. The product k r can be visualized as the orientation of a rotating “clock hand.”

For a particle traveling from slit 1 to a screen position x, this can be summarized as:

“The particle travels from slit 1 to screen position x, accumulating a phase determined by the distance traveled along that path.”

This phase information will be used to construct the complex probability amplitudes whose superposition produces the observed interference pattern.






3. Constructing Complex Probability Amplitudes:
   
- What is a complex probability amplitude?
     
 A complex probability amplitude is an unobservable complex quantity whose magnitude squared gives the probability of a measurement outcome and whose phase controls interference effects. It is a mathematical object that behaves like a wave in order to encode phase information, but it does not represent a physical wave height and is not directly measurable.

In quantum mechanics, probabilities are not assigned directly to paths or positions. Instead, complex probability amplitudes are assigned to possible paths, and measurable probabilities are obtained only after amplitudes are combined and their magnitudes squared.


- Why not use the amplitude where the wave "hits" the screen?
  
In the double-slit experiment, we do not observe a physical wave striking the screen. Electrons arrive as discrete particles, yet the distribution of their arrival positions exhibits wave-like interference. There is no observable wave height to measure—only detection events.

As Richard Feynman describes:

“The electrons arrive in lumps like particles, and the probability of arrival of these lumps is distributed like the distribution of intensity of a wave.”


- Why must the the amplitudes be complex?
  
  Interference requires:
  - cancellation
  - reinforcement
  - sensitivity to relative phase

Real-valued amplitudes alone cannot robustly encode this information. Complex numbers allow phase to be represented as a rotation, enabling amplitudes to add coherently and interfere.

- A real-valued amplitude can be viewed as a projection of a complex amplitude onto a single axis, losing directional phase information. In this sense:

- A real amplitude is a shadow of a complex probability amplitude.

The shadow retains only partial information, while the full complex amplitude preserves the phase relationships necessary to model interference correctly.


- What information does the complex probability amplitude carry?
  A complex probability amplitude encodes:
  - phase information, often visualized as a rotating clock hand
  - relative timing between different possible paths
  - the ability for amplitudes to interfere constructively or destructively

This information is not directly observable but becomes physically meaningful when amplitudes are combined and converted into probabilities via the magnitude-squared rule.






4. Computing the Measureable Probability Density:
   
Once the complex probability amplitudes from each slit have been constructed, they are combined to form a total amplitude:

ψ(x) = ψ₁(x) + ψ₂(x).

The measurable probability density is then obtained by taking the magnitude squared of the total amplitude:

P(x) = |ψ(x)|².

Interference arises because amplitudes are added before probabilities are computed. If probabilities were added directly, the result would correspond to a classical mixture and no interference pattern would appear.

Superposition and which-path detection:
In the absence of measurement, it is not possible to determine which slit the particle passed through. Introducing a detector provides which-path information and destroys the phase coherence between alternatives, eliminating interference and producing classical behavior.

Because the path information is unobserved, quantum mechanics requires that contributions from both slits be treated as simultaneously possible and combined at the level of complex probability amplitudes. The particle is therefore described by a superposition of alternatives, not by a definite trajectory.

Adding amplitudes prior to measurement produces cross terms when the magnitude squared is taken. These cross terms are responsible for the characteristic interference fringes observed on the screen.


Why the magnitude square is taken:

Probabilities in quantum mechanics are obtained by taking the magnitude squared of the complex probability amplitude:

|ψ|² = ψ* ψ.

This operation guarantees that probabilities are:
- real
- nonnegative
- physically meaningful

Squaring the complex amplitude itself would not, in general, yield a real quantity and therefore cannot represent a probability.


Interference and observable results:

Interference does not arise from squaring a single amplitude, which would yield a uniform probability distribution. Instead, it arises from adding multiple complex amplitudes and then taking the magnitude squared of their sum. This process generates interference terms that depend on the relative phase between paths.

The resulting probability density is a continuous distribution across the screen. Regions of constructive interference correspond to higher probability density, while regions of destructive interference correspond to lower probability density.

If individual particle detections are later simulated, a histogram of detection events will approximate this continuous probability distribution as the number of detected particles increases.





Final Note:

This experiment demonstrates that interference is not a property of particles following classical trajectories, but a consequence of quantum superposition and phase coherence. By modeling amplitudes rather than probabilities, the interference pattern emerges naturally, illustrating the fundamentally quantum nature of the double-slit experiment.











# How to run the program
After cloning the repository and navigating into it, run:

```bash
python Main.py
