---
layout: default
title: TIM-PRM: Verifying multimodal reasoning with Tool-Integrated PRM
---

# TIM-PRM: Verifying multimodal reasoning with Tool-Integrated PRM

**arXiv**: [2511.22998v1](https://arxiv.org/abs/2511.22998) | [PDF](https://arxiv.org/pdf/2511.22998.pdf)

**作者**: Peng Kuang, Xiangxiang Wang, Wentao Liu, Jian Dong, Kaidi Xu, Haohan Wang

---

## 💡 一句话要点

**提出TIM-PRM框架，通过工具集成主动验证解决多模态大语言模型推理中的幻觉与逻辑不一致问题。**

**关键词**: `多模态大语言模型` `过程奖励模型` `工具集成验证` `视觉幻觉缓解` `主动推理框架` `独立提问机制`

## 📋 核心要点

1. 多模态大语言模型在数学推理中易受视觉幻觉和逻辑不一致影响，标准监督方法难以缓解。
2. TIM-PRM将验证转化为主动工具增强调查，训练模型规划策略并使用独立提问机制查询证据以消除确认偏差。
3. 在VisualProcessBench实验中，8B参数模型超越开源多模态PRMs，优于更大模型如Qwen2.5-72B，并提供可解释验证过程。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved impressive performances in mathematical reasoning, yet they remain vulnerable to visual hallucinations and logical inconsistencies that standard outcome-based supervision fails to mitigate. While Process Reward Models (PRMs) promise step-by-step verification, current approaches typically operate as scalar scorers or generative critics that suffer from sycophancy, blindly validating the flawed hypotheses rather than grounding them in visual reality. To bridge this gap, we introduce TIM-PRM (Tool-Integrated Multimodal PRM), a novel agentic framework that transforms verification from a passive classification task into an active, tool-augmented investigation. TIM-PRM is trained to explicitly plan verification strategies and utilizes a mechanism of Independent Question Asking to query evidence via external tools, effectively decoupling verification from the reasoning context to eliminate confirmation bias. We instantiate this method by curating a high-quality dataset of tool-integrated verification trajectories. Extensive experiments on VisualProcessBench demonstrate that our 8B parameter model surpasses existing open-source multimodal PRMs, significantly outperforming much larger models like Qwen2.5-72B and InternVL-78B, while offering interpretable insights into the verification process.

