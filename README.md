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

Results:
<img width="472" height="359" alt="image" src="https://github.com/user-attachments/assets/ff839abc-fdae-457a-a392-7d8d8d2b8a96" />

The classical double-slit experiment produces a probability distribution consisting of two smooth Gaussian peaks, each corresponding to one of the slits. The peaks are centered at positions aligned with the slit locations, and their similar heights indicate an equal probability for particles to pass through either slit. The continuous, non-oscillatory shape of the distribution reflects the statistical independence of particle arrivals and the absence of any interference effects. Consistent with classical mechanics, the observed pattern is simply the sum of two independent single-slit distributions and exhibits no interference fringes.This result establishes a classical baseline and highlights the inability of classical probability theory to produce interference patterns.


## Experiment 3: Double-Slit Measurement (Observed Result, No Path Detection)

When the double-slit experiment is performed without any measurement that determines which slit an electron passes through, the observed probability distribution on the screen exhibits an interference pattern rather than the independent smooth distributions predicted by classical probability theory. This behavior cannot be explained by treating electrons as classical particles following definite trajectories.

<img width="354" height="134" alt="image" src="https://github.com/user-attachments/assets/aec05c47-97b9-4b75-bd0e-8b0f075185f7" />

Instead, the results are consistent with a quantum description in which electrons are represented by complex probability amplitudes that propagate through both slits simultaneously. These amplitudes carry phase information and interfere when combined, producing regions of constructive and destructive interference on the detection screen. In this experiment, we model the observed double-slit interference pattern by replacing classical probability addition with quantum amplitude superposition, demonstrating how interference arises as a purely quantum effect.


Results:




# How to run the program
After cloning the repository and navigating into it, run:

```bash
python Main.py
