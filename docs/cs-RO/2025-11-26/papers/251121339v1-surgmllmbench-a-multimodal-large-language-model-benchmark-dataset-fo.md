---
layout: default
title: SurgMLLMBench: A Multimodal Large Language Model Benchmark Dataset for Surgical Scene Understanding
---

# SurgMLLMBench: A Multimodal Large Language Model Benchmark Dataset for Surgical Scene Understanding

**arXiv**: [2511.21339v1](https://arxiv.org/abs/2511.21339) | [PDF](https://arxiv.org/pdf/2511.21339.pdf)

**作者**: Tae-Min Choi, Tae Kyeong Jeong, Garam Kim, Jaemin Lee, Yeongyoon Koh, In Cheul Choi, Jae-Ho Chung, Jong Woong Park, Juyoun Park

---

## 💡 一句话要点

**提出SurgMLLMBench基准以解决手术场景理解中多模态LLM评估不一致问题**

**关键词**: `多模态大语言模型` `手术场景理解` `像素级分割` `视觉问答基准` `跨域泛化`

## 📋 核心要点

1. 现有手术数据集多为VQA格式，分类不统一且缺乏像素级分割，限制多模态LLM评估
2. 集成像素级分割掩码和结构化VQA注释，覆盖腹腔镜、机器人辅助和显微手术领域
3. 实验显示单一模型在跨域评估中表现一致，并能泛化到未知数据集

## 📄 摘要（原文）

> Recent advances in multimodal large language models (LLMs) have highlighted their potential for medical and surgical applications. However, existing surgical datasets predominantly adopt a Visual Question Answering (VQA) format with heterogeneous taxonomies and lack support for pixel-level segmentation, limiting consistent evaluation and applicability. We present SurgMLLMBench, a unified multimodal benchmark explicitly designed for developing and evaluating interactive multimodal LLMs for surgical scene understanding, including the newly collected Micro-surgical Artificial Vascular anastomosIS (MAVIS) dataset. It integrates pixel-level instrument segmentation masks and structured VQA annotations across laparoscopic, robot-assisted, and micro-surgical domains under a unified taxonomy, enabling comprehensive evaluation beyond traditional VQA tasks and richer visual-conversational interactions. Extensive baseline experiments show that a single model trained on SurgMLLMBench achieves consistent performance across domains and generalizes effectively to unseen datasets. SurgMLLMBench will be publicly released as a robust resource to advance multimodal surgical AI research, supporting reproducible evaluation and development of interactive surgical reasoning models.

