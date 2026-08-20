# AI Action Board

Last Updated: 2026-08-20 15:25:47

1. **Security Audit:** Evaluate if current API implementations can migrate to OpenAI’s Zero Data Retention (ZDR) mode to enhance data security.
2. **Infrastructure Optimization:** Review GPU cluster management protocols; a 30% increase in utilization is achievable through better scheduling (per the Dharma AI findings).
3. **RAG Upgrade:** Instruct technical teams to explore "Multi-Vector" embedding models to improve the accuracy of internal knowledge bases.

## Technology Trends
- **Quantization-Aware Distillation (QAD):** The trend of making models smaller and smarter simultaneously, rather than just "larger."
- **Edge Intelligence:** A shift toward running frontier-level models on local or limited hardware.
- **Late Interaction Retrieval:** Moving beyond simple vector search to more complex, multi-vector interactions for better data retrieval.
- **AI Literacy as Infrastructure:** Transitioning from treating AI as a "perk" to a foundational skill in education and national security.

## Terminology
- **Zero Data Retention (ZDR):** A privacy setting where the AI provider does not store the data sent via API, ensuring it isn't used for training or viewed by humans.
- **Quantization:** The process of reducing the precision of a model's numbers (e.g., from 16-bit to 4-bit) to make it run faster and use less memory.
- **Distillation:** Teaching a smaller "student" model to mimic the behavior and performance of a larger "teacher" model.
- **Multi-Vector Embedding:** A way of representing text where multiple "points" are used instead of one, allowing the AI to understand complex relationships in data much better.
- **GPU Utilization:** A measure of how much of a graphics chip's total computing power is actually being used at any given moment.
- **Late Interaction:** A retrieval method that compares different parts of a query and a document separately before combining them, leading to much more accurate search results.