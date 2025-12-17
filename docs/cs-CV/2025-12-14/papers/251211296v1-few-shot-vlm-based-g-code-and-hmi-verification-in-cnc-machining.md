---
layout: default
title: Few-Shot VLM-Based G-Code and HMI Verification in CNC Machining
---

# Few-Shot VLM-Based G-Code and HMI Verification in CNC Machining

**arXiv**: [2512.11296v1](https://arxiv.org/abs/2512.11296) | [PDF](https://arxiv.org/pdf/2512.11296.pdf)

**作者**: Yasaman Hashem Pour, Nazanin Mahjourian, Vinh Nguyen

---

## 💡 一句话要点

**提出基于少样本视觉语言模型的G代码和HMI验证方法，用于CNC加工中的综合调试。**

**关键词**: `少样本学习` `视觉语言模型` `G代码验证` `人机界面` `CNC加工` `综合调试`

## 📋 核心要点

1. 核心问题：CNC加工中G代码验证需结合HMI视觉信息，但现有LLM方法无法处理视觉模态。
2. 方法要点：使用少样本VLM，基于结构化JSON提示，同时评估G代码文本和HMI截图中的错误。
3. 实验或效果：在15-slant-PRO车床数据集上，少样本提示相比零-shot提升了HMI错误检测和G代码不一致性识别。

## 📄 摘要（原文）

> Manual generation of G-code is important for learning the operation of CNC machines. Prior work in G-code verification uses Large-Language Models (LLMs), which primarily examine errors in the written programming. However, CNC machining requires extensive use and knowledge of the Human-Machine Interface (HMI), which displays machine status and errors. LLMs currently lack the capability to leverage knowledge of HMIs due to their inability to access the vision modality. This paper proposes a few-shot VLM-based verification approach that simultaneously evaluates the G-code and the HMI display for errors and safety status. The input dataset includes paired G-code text and associated HMI screenshots from a 15-slant-PRO lathe, including both correct and error-prone cases. To enable few-shot learning, the VLM is provided with a structured JSON schema based on prior heuristic knowledge. After determining the prompts, instances of G-code and HMI that either contain errors or are error free are used as few-shot examples to guide the VLM. The model was then evaluated in comparison to a zero-shot VLM through multiple scenarios of incorrect G-code and HMI errors with respect to per-slot accuracy. The VLM showed that few-shot prompting led to overall enhancement of detecting HMI errors and discrepancies with the G-code for more comprehensive debugging. Therefore, the proposed framework was demonstrated to be suitable for verification of manually generated G-code that is typically developed in CNC training.

