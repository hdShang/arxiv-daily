---
layout: default
title: Refine and Align: Confidence Calibration through Multi-Agent Interaction in VQA
---

# Refine and Align: Confidence Calibration through Multi-Agent Interaction in VQA

**arXiv**: [2511.11169v1](https://arxiv.org/abs/2511.11169) | [PDF](https://arxiv.org/pdf/2511.11169.pdf)

**作者**: Ayush Pandey, Jai Bardhan, Ishita Jain, Ramya S Hebbalaguppe, Rohan Raju Dhanakshirur, Lovekesh Vig

---

## 💡 一句话要点

**提出AlignVQA多智能体框架以解决VQA中置信度校准问题**

**关键词**: `视觉问答` `置信度校准` `多智能体系统` `辩论框架` `校准损失函数`

## 📋 核心要点

1. VQA系统在视觉不确定性下常产生过度自信，影响高风险应用可靠性。
2. 采用多智能体辩论框架，通过专业代理生成答案并交互优化置信度估计。
3. 实验显示校准误差显著降低，新损失函数提升个体代理置信度质量。

## 📄 摘要（原文）

> In the context of Visual Question Answering (VQA) and Agentic AI, calibration refers to how closely an AI system's confidence in its answers reflects their actual correctness. This aspect becomes especially important when such systems operate autonomously and must make decisions under visual uncertainty. While modern VQA systems, powered by advanced vision-language models (VLMs), are increasingly used in high-stakes domains like medical diagnostics and autonomous navigation due to their improved accuracy, the reliability of their confidence estimates remains under-examined. Particularly, these systems often produce overconfident responses. To address this, we introduce AlignVQA, a debate-based multi-agent framework, in which diverse specialized VLM -- each following distinct prompting strategies -- generate candidate answers and then engage in two-stage interaction: generalist agents critique, refine and aggregate these proposals. This debate process yields confidence estimates that more accurately reflect the model's true predictive performance. We find that more calibrated specialized agents produce better aligned confidences. Furthermore, we introduce a novel differentiable calibration-aware loss function called aligncal designed to fine-tune the specialized agents by minimizing an upper bound on the calibration error. This objective explicitly improves the fidelity of each agent's confidence estimates. Empirical results across multiple benchmark VQA datasets substantiate the efficacy of our approach, demonstrating substantial reductions in calibration discrepancies. Furthermore, we propose a novel differentiable calibration-aware loss to fine-tune the specialized agents and improve the quality of their individual confidence estimates based on minimising upper bound calibration error.

