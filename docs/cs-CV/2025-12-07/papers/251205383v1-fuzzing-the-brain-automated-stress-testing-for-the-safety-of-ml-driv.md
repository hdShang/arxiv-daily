---
layout: default
title: Fuzzing the brain: Automated stress testing for the safety of ML-driven neurostimulation
---

# Fuzzing the brain: Automated stress testing for the safety of ML-driven neurostimulation

**arXiv**: [2512.05383v1](https://arxiv.org/abs/2512.05383) | [PDF](https://arxiv.org/pdf/2512.05383.pdf)

**作者**: Mara Downing, Matthew Peng, Jacob Granley, Michael Beyeler, Tevfik Bultan

---

## 💡 一句话要点

**提出基于覆盖引导模糊测试的方法，以检测ML驱动神经刺激系统中的不安全刺激模式。**

**关键词**: `神经刺激安全` `模糊测试` `机器学习模型验证` `生物物理限制` `覆盖引导测试` `神经接口`

## 📋 核心要点

1. 核心问题：ML模型在神经假体设备中生成刺激模式时，可能输出违反生物物理安全限制的风险。
2. 方法要点：采用覆盖引导模糊测试，扰动模型输入并追踪刺激是否超出电荷密度、瞬时电流或电极共激活等安全限制。
3. 实验或效果：应用于视网膜和皮层刺激编码器，系统揭示多种超出安全限制的刺激模式，并通过覆盖指标实现可解释的架构比较。

## 📄 摘要（原文）

> Objective: Machine learning (ML) models are increasingly used to generate electrical stimulation patterns in neuroprosthetic devices such as visual prostheses. While these models promise precise and personalized control, they also introduce new safety risks when model outputs are delivered directly to neural tissue. We propose a systematic, quantitative approach to detect and characterize unsafe stimulation patterns in ML-driven neurostimulation systems. Approach: We adapt an automated software testing technique known as coverage-guided fuzzing to the domain of neural stimulation. Here, fuzzing performs stress testing by perturbing model inputs and tracking whether resulting stimulation violates biophysical limits on charge density, instantaneous current, or electrode co-activation. The framework treats encoders as black boxes and steers exploration with coverage metrics that quantify how broadly test cases span the space of possible outputs and violation types. Main results: Applied to deep stimulus encoders for the retina and cortex, the method systematically reveals diverse stimulation regimes that exceed established safety limits. Two violation-output coverage metrics identify the highest number and diversity of unsafe outputs, enabling interpretable comparisons across architectures and training strategies. Significance: Violation-focused fuzzing reframes safety assessment as an empirical, reproducible process. By transforming safety from a training heuristic into a measurable property of the deployed model, it establishes a foundation for evidence-based benchmarking, regulatory readiness, and ethical assurance in next-generation neural interfaces.

