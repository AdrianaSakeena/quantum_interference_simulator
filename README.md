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


# How to run the program
After cloning the repository and navigating into it, run:

```bash
python Main.py
