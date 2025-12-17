---
layout: default
title: AgriCoT: A Chain-of-Thought Benchmark for Evaluating Reasoning in Vision-Language Models for Agriculture
---

# AgriCoT: A Chain-of-Thought Benchmark for Evaluating Reasoning in Vision-Language Models for Agriculture

**arXiv**: [2511.23253v1](https://arxiv.org/abs/2511.23253) | [PDF](https://arxiv.org/pdf/2511.23253.pdf)

**作者**: Yibin Wen, Qingmei Li, Zi Ye, Jiarui Zhang, Jing Wu, Zurong Mai, Shuohong Lou, Yuhang Chen, Henglian Huang, Xiaoya Fan, Yang Zhang, Lingyuan Zhao, Haohuan Fu, Huang Jianxi, Juepeng Zheng

---

## 💡 一句话要点

**提出AgriCoT基准以评估农业视觉语言模型的推理能力**

**关键词**: `视觉语言模型` `农业视觉问答` `思维链推理` `零样本评估` `基准数据集`

## 📋 核心要点

1. 现有VQA基准在农业复杂场景中评估推理能力不足
2. AgriCoT集成思维链推理，包含4,535个样本，专注逻辑推理与问题解决
3. 评估26个VLM显示专有模型答题强但推理能力存在显著差距

## 📄 摘要（原文）

> Recent advancements in Vision-Language Models (VLMs) have significantly transformed various industries. In agriculture, these dual-modal capabilities offer promising applications such as precision farming, crop monitoring, pest detection, and environmental sustainability. While several Visual Question Answering (VQA) datasets and benchmarks have been developed to evaluate VLM performance, they often fail to adequately assess the critical reasoning and problem-solving skills required in complex agricultural contexts. To address this gap, we introduce AgriCoT, a VQA dataset that incorporates Chain-of-Thought (CoT) reasoning, specifically designed to evaluate the reasoning capabilities of VLMs. With 4,535 carefully curated samples, AgriCoT offers a comprehensive and robust evaluation of reasoning abilities for VLMs, particularly in zero-shot scenarios, by focusing on their capacity to engage in logical reasoning and effective problem-solving. Our evaluations, conducted with 26 representative VLMs, including both proprietary and open-source models, reveal that while some proprietary models excel at answering questions, there is a notable and significant gap in their reasoning capabilities. This underscores the importance of incorporating CoT for more precise and effective assessments. Our dataset are available at https://huggingface.co/datasets/wenyb/AgriCoT.

