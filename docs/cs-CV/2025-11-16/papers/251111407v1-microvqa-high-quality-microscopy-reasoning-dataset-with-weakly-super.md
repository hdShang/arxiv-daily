---
layout: default
title: MicroVQA++: High-Quality Microscopy Reasoning Dataset with Weakly Supervised Graphs for Multimodal Large Language Model
---

# MicroVQA++: High-Quality Microscopy Reasoning Dataset with Weakly Supervised Graphs for Multimodal Large Language Model

**arXiv**: [2511.11407v1](https://arxiv.org/abs/2511.11407) | [PDF](https://arxiv.org/pdf/2511.11407.pdf)

**作者**: Manyu Li, Ruian He, Chenxi Ma, Weimin Tan, Bo Yan

---

## 💡 一句话要点

**提出MicroVQA++数据集与HiCQA-Graph方法以解决显微镜推理数据稀缺问题**

**关键词**: `显微镜视觉问答` `多模态大语言模型` `异构图过滤` `数据质量控制` `生物医学成像`

## 📋 核心要点

1. 显微镜推理受限于大规模高质量训练数据的稀缺
2. 使用三阶段方法构建数据集，包括专家引导、图过滤和MLLM生成
3. 实验显示4B规模MLLM在显微镜推理中达到竞争性性能

## 📄 摘要（原文）

> Multimodal Large Language Models are increasingly applied to biomedical imaging, yet scientific reasoning for microscopy remains limited by the scarcity of large-scale, high-quality training data. We introduce MicroVQA++, a three-stage, large-scale and high-quality microscopy VQA corpus derived from the BIOMEDICA archive. Stage one bootstraps supervision from expert-validated figure-caption pairs sourced from peer-reviewed articles. Stage two applies HiCQA-Graph, a novel heterogeneous graph over images, captions, and QAs that fuses NLI-based textual entailment, CLIP-based vision-language alignment, and agent signals to identify and filter inconsistent samples. Stage three uses a MultiModal Large Language Model (MLLM) agent to generate multiple-choice questions (MCQ) followed by human screening. The resulting release comprises a large training split and a human-checked test split whose Bloom's level hard-sample distribution exceeds the MicroVQA benchmark. Our work delivers (i) a quality-controlled dataset that couples expert literature with graph-based filtering and human refinement; (ii) HiCQA-Graph, the first graph that jointly models (image, caption, QA) for cross-modal consistency filtering; (iii) evidence that careful data construction enables 4B-scale MLLMs to reach competitive microscopy reasoning performance (e.g., GPT-5) and achieve state-of-the-art performance among open-source MLLMs. Code and dataset will be released after the review process concludes.

