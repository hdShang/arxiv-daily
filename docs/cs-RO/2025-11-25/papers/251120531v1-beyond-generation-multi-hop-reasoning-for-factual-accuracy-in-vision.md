---
layout: default
title: Beyond Generation: Multi-Hop Reasoning for Factual Accuracy in Vision-Language Models
---

# Beyond Generation: Multi-Hop Reasoning for Factual Accuracy in Vision-Language Models

**arXiv**: [2511.20531v1](https://arxiv.org/abs/2511.20531) | [PDF](https://arxiv.org/pdf/2511.20531.pdf)

**作者**: Shamima Hossain

---

## 💡 一句话要点

**提出知识引导多跳推理框架以提升视觉语言模型的事实准确性**

**关键词**: `视觉语言模型` `多跳推理` `知识图谱` `事实准确性` `图像描述任务`

## 📋 核心要点

1. 视觉语言模型生成内容常因推理能力不足而事实错误
2. 利用知识图谱进行多步推理，包括实体识别和图遍历
3. 实验显示事实准确性提升约31%，分析不同知识表示效果

## 📄 摘要（原文）

> Visual Language Models (VLMs) are powerful generative tools but often produce factually in- accurate outputs due to a lack of robust reason- ing capabilities. While extensive research has been conducted on integrating external knowl- edge for reasoning in large language models (LLMs), such efforts remain underexplored in VLMs, where the challenge is compounded by the need to bridge multiple modalities seam- lessly. This work introduces a framework for knowledge-guided reasoning in VLMs, leverag- ing structured knowledge graphs for multi-hop verification using image-captioning task to il- lustrate our framework. Our approach enables systematic reasoning across multiple steps, in- cluding visual entity recognition, knowledge graph traversal, and fact-based caption refine- ment. We evaluate the framework using hi- erarchical, triple-based and bullet-point based knowledge representations, analyzing their ef- fectiveness in factual accuracy and logical infer- ence. Empirical results show that our approach improves factual accuracy by approximately 31% on preliminary experiments on a curated dataset of mixtures from Google Landmarks v2, Conceptual captions and Coco captions re- vealing key insights into reasoning patterns and failure modes. This work demonstrates the po- tential of integrating external knowledge for advancing reasoning in VLMs, paving the way for more reliable and knowledgable multimodal systems.

