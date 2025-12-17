---
layout: default
title: Probing the effectiveness of World Models for Spatial Reasoning through Test-time Scaling
---

# Probing the effectiveness of World Models for Spatial Reasoning through Test-time Scaling

**arXiv**: [2512.05809v1](https://arxiv.org/abs/2512.05809) | [PDF](https://arxiv.org/pdf/2512.05809.pdf)

**作者**: Saurav Jha, M. Jehanzeb Mirza, Wei Lin, Shiqi Yang, Sarath Chandar

---

## 💡 一句话要点

**提出ViSA框架以改进世界模型在空间推理中的测试时验证效果**

**关键词**: `空间推理` `测试时缩放` `世界模型` `视觉语言模型` `验证框架`

## 📋 核心要点

1. 核心问题：视觉语言模型在需要多视角理解的空间推理任务中表现有限，现有测试时验证方法存在校准不足和偏差问题。
2. 方法要点：引入基于空间断言的验证框架，通过可验证的帧锚定微声明来改进奖励信号，减少轨迹选择偏差。
3. 实验或效果：在SAT-Real基准上提升空间推理性能，但在MMSI-Bench上未实现一致改进，揭示世界模型的信息瓶颈。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) remain limited in spatial reasoning tasks that require multi-view understanding and embodied perspective shifts. Recent approaches such as MindJourney attempt to mitigate this gap through test-time scaling where a world model imagines action-conditioned trajectories and a heuristic verifier selects helpful views from such trajectories. In this work, we systematically examine how such test-time verifiers behave across benchmarks, uncovering both their promise and their pitfalls. Our uncertainty-based analyses show that MindJourney's verifier provides little meaningful calibration, and that random scoring often reduces answer entropy equally well, thus exposing systematic action biases and unreliable reward signals. To mitigate these, we introduce a Verification through Spatial Assertions (ViSA) framework that grounds the test-time reward in verifiable, frame-anchored micro-claims. This principled verifier consistently improves spatial reasoning on the SAT-Real benchmark and corrects trajectory-selection biases through more balanced exploratory behavior. However, on the challenging MMSI-Bench, none of the verifiers, including ours, achieve consistent scaling, suggesting that the current world models form an information bottleneck where imagined views fail to enrich fine-grained reasoning. Together, these findings chart the bad, good, and ugly aspects of test-time verification for world-model-based reasoning. Our code is available at https://github.com/chandar-lab/visa-for-mindjourney.

