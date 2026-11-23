# AI Action Board

Last Updated: 2026-11-23 14:53:35

1. **Audit Fine-Tuning Pipelines:** Re-evaluate training cost estimation models to account for memory bandwidth and communication overhead rather than relying solely on raw FLOP counters.
2. **Implement Agentic Evals:** Transition quality assurance teams from static prompt-response testing to dynamic agentic evaluation harnesses before releasing autonomous features.
3. **Review Model Theft Defenses:** If serving custom/proprietary fine-tuned models externally, implement rate-limiting, anomaly query detection, and output watermarking to defend against adversarial distillation.
4. **Explore Compact Models for Edge Workloads:** Test sub-30B models (e.g., DaisyRose-27B, Inkling 2 Mini) for internal latency-sensitive or privacy-restricted use cases.