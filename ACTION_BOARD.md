# AI Action Board

Last Updated: 2026-07-19 21:43:21

1.  **Adopt the Scorecard:** Finance and Tech teams should align on the "Return on Compute" and "Cost per Successful Task" metrics for all current AI initiatives.
2.  **Audit Secrets Management:** Following the Hugging Face incident, conduct a security audit of how AI API keys and model weights are stored.
3.  **Explore Model Routing:** Evaluate whether our current architecture can implement a "router" to save costs on high-volume, low-complexity tasks.

## Technology Trends
*   **Agentic Workflows:** Moving away from single-turn prompts toward multi-step, autonomous task execution.
*   **Automated Red Teaming:** Using AI to find the flaws in other AI systems to speed up the safety cycle.
*   **Multi-Model Orchestration:** Companies are no longer using one model; they are building "swarms" or "routes" where different models handle different tasks based on complexity and cost.

## Terminology

*   **ROI (Return on Investment):** In AI, this is now being measured as the value of the work an AI performs minus the cost of the compute/API calls.
*   **Red Teaming:** The process of "attacking" an AI system to find its weaknesses, biases, or safety flaws.
*   **Agentic Workflow:** A system where an AI doesn't just talk, but takes actions (like sending emails or updating a database) to complete a goal.
*   **Model Routing:** A traffic-control system for AI that sends easy questions to small, cheap models and hard questions to large, expensive ones.
*   **Return on Compute:** A metric measuring how much business value is generated for every unit of processing power used.
*   **Fine-tuning:** Taking a "pre-trained" AI and giving it extra training on a specific set of data to make it an expert in one area.