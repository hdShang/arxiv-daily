---
layout: default
title: MemLoRA: Distilling Expert Adapters for On-Device Memory Systems
---

# MemLoRA: Distilling Expert Adapters for On-Device Memory Systems

**arXiv**: [2512.04763v1](https://arxiv.org/abs/2512.04763) | [PDF](https://arxiv.org/pdf/2512.04763.pdf)

**作者**: Massimo Bini, Ondrej Bohdal, Umberto Michieli, Zeynep Akata, Mete Ozay, Taha Ceritli

---

## 💡 一句话要点

**提出MemLoRA与MemLoRA-V，通过蒸馏专家适配器实现设备端内存系统，支持文本与视觉任务。**

**关键词**: `设备端内存系统` `专家适配器蒸馏` `小语言模型` `视觉语言模型` `多模态推理` `知识蒸馏`

## 📋 核心要点

1. 问题：LLM内存增强系统成本高，SLM性能不足，且缺乏视觉能力，限制设备端与多模态应用。
2. 方法：为SLM和SVLM训练专用内存适配器，基于知识蒸馏，分别处理知识提取、更新和生成操作。
3. 效果：在文本任务上超越大模型基线，视觉任务上大幅提升准确率，保持设备端部署优势。

## 📄 摘要（原文）

> Memory-augmented Large Language Models (LLMs) have demonstrated remarkable consistency during prolonged dialogues by storing relevant memories and incorporating them as context. Such memory-based personalization is also key in on-device settings that allow users to keep their conversations and data private. However, memory-augmented systems typically rely on LLMs that are too costly for local on-device deployment. Even though Small Language Models (SLMs) are more suitable for on-device inference than LLMs, they cannot achieve sufficient performance. Additionally, these LLM-based systems lack native visual capabilities, limiting their applicability in multimodal contexts. In this paper, we introduce (i) MemLoRA, a novel memory system that enables local deployment by equipping SLMs with specialized memory adapters, and (ii) its vision extension MemLoRA-V, which integrates small Vision-Language Models (SVLMs) to memory systems, enabling native visual understanding. Following knowledge distillation principles, each adapter is trained separately for specific memory operations$\unicode{x2013}$knowledge extraction, memory update, and memory-augmented generation. Equipped with memory adapters, small models enable accurate on-device memory operations without cloud dependency. On text-only operations, MemLoRA outperforms 10$\times$ larger baseline models (e.g., Gemma2-27B) and achieves performance comparable to 60$\times$ larger models (e.g., GPT-OSS-120B) on the LoCoMo benchmark. To evaluate visual understanding operations instead, we extend LoCoMo with challenging Visual Question Answering tasks that require direct visual reasoning. On this, our VLM-integrated MemLoRA-V shows massive improvements over caption-based approaches (81.3 vs. 23.7 accuracy) while keeping strong performance in text-based tasks, demonstrating the efficacy of our method in multimodal contexts.

