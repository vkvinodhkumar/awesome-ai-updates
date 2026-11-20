# AI Terminology

Last Updated: 2026-11-20 02:24:01

*   **Performance Factory:** An automated internal system that uses code-generating AI models to continuously identify, diagnose, and resolve software performance bottlenecks.
*   **Mixture of Experts (MoE):** An architecture that routes input data to specific sub-networks ("experts"), allowing a model to have a massive total parameter size while keeping active inference compute overhead low.
*   **Expert Streaming / Offloading:** A technical strategy that keeps dormant model weights in system RAM or NVMe storage and dynamically transfers active experts into GPU VRAM only when needed.
*   **Post-Training Efficiency:** Optimization techniques (such as alignment, direct preference optimization, and fine-tuning refinement) applied after initial base training to increase model performance without full re-training costs.
*   **FLOPs (Floating Point Operations):** A measure of theoretical hardware compute performance; often used to estimate training time, though real-world performance is strongly influenced by data transfer speeds and memory bandwidth.
*   **Time-Series Model:** An AI model engineered specifically to analyze data points indexed in temporal order, used extensively for financial forecasting, telemetry, and sensor monitoring.
*   **PR (Pull Request) Scan:** Automated analysis triggered during developer code reviews to evaluate security, quality, and logic prior to merging code into the main codebase.