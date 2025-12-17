---
layout: default
title: When Privacy Meets Recovery: The Overlooked Half of Surrogate-Driven Privacy Preservation for MLLM Editing
---

# When Privacy Meets Recovery: The Overlooked Half of Surrogate-Driven Privacy Preservation for MLLM Editing

**arXiv**: [2512.07166v1](https://arxiv.org/abs/2512.07166) | [PDF](https://arxiv.org/pdf/2512.07166.pdf)

**作者**: Siyuan Xu, Yibing Liu, Peilin Chen, Yung-Hui Li, Shiqi Wang, Sam Kwong

---

## 💡 一句话要点

**提出统一方法以恢复多模态大语言模型编辑中的隐私内容，平衡保护与可用性。**

**关键词**: `多模态大语言模型` `隐私保护` `隐私恢复` `引导生成` `数据集构建` `编辑保真度`

## 📋 核心要点

1. 核心问题：现有隐私保护方法忽视隐私恢复质量评估，导致隐私泄露问题未全面解决。
2. 方法要点：将隐私恢复建模为基于多模态信号的引导生成任务，可靠重建隐私内容并保持编辑保真度。
3. 实验或效果：在SPPE和InstructPix2Pix数据集上验证，方法泛化性强，在多样视觉内容和编辑任务中表现良好。

## 📄 摘要（原文）

> Privacy leakage in Multimodal Large Language Models (MLLMs) has long been an intractable problem. Existing studies, though effectively obscure private information in MLLMs, often overlook the evaluation of the authenticity and recovery quality of user privacy. To this end, this work uniquely focuses on the critical challenge of how to restore surrogate-driven protected data in diverse MLLM scenarios. We first bridge this research gap by contributing the SPPE (Surrogate Privacy Protected Editable) dataset, which includes a wide range of privacy categories and user instructions to simulate real MLLM applications. This dataset offers protected surrogates alongside their various MLLM-edited versions, thus enabling the direct assessment of privacy recovery quality. By formulating privacy recovery as a guided generation task conditioned on complementary multimodal signals, we further introduce a unified approach that reliably reconstructs private content while preserving the fidelity of MLLM-generated edits. The experiments on both SPPE and InstructPix2Pix further show that our approach generalizes well across diverse visual content and editing tasks, achieving a strong balance between privacy protection and MLLM usability.

