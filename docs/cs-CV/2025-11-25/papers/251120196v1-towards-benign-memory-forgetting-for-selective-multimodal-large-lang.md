---
layout: default
title: Towards Benign Memory Forgetting for Selective Multimodal Large Language Model Unlearning
---

# Towards Benign Memory Forgetting for Selective Multimodal Large Language Model Unlearning

**arXiv**: [2511.20196v1](https://arxiv.org/abs/2511.20196) | [PDF](https://arxiv.org/pdf/2511.20196.pdf)

**作者**: Zhen Zeng, Leijiang Gu, Zhangling Duan, Feng Li, Zenglin Shi, Cees G. M. Snoek, Meng Wang

---

## 💡 一句话要点

**提出SMFA适配器以解决多模态大模型选择性遗忘中的性能退化问题**

**关键词**: `选择性遗忘` `多模态大语言模型` `隐私保护` `适配器微调` `基准评估`

## 📋 核心要点

1. 多模态大语言模型可能无意记忆隐私敏感信息，现有遗忘方法易损害模型通用图像理解能力。
2. SMFA通过微调生成遗忘适配器，并使用保留锚点引导掩码机制，隔离遗忘区域。
3. 实验表明SMFA在S-MLLMUn基准上实现精确可控遗忘，同时保持基础图像理解性能。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) achieve remarkable capabilities but can inadvertently memorize privacy-sensitive information. Although existing unlearning methods can remove such knowledge, they fail to achieve benign forgetting because they often degrade the model's general image understanding performance. To address this, we propose the Sculpted Memory Forgetting Adapter (SMFA), which confines forgetting to targeted memory regions while preserving overall capabilities. SMFA first fine-tunes the model to replace sensitive responses with refusals, yielding a memory forgetting adapter, and then applies a retaining anchor-guided masking mechanism to prevent interference with unrelated knowledge and understanding ability. To systematically evaluate selective MLLM unlearning, we introduce S-MLLMUn Bench, the first benchmark designed to jointly assess the removal of sensitive knowledge and retention of general visual understanding. Extensive experiments show that, unlike prior methods, SMFA achieves precise and controllable unlearning while maintaining the model's foundational image understanding.

