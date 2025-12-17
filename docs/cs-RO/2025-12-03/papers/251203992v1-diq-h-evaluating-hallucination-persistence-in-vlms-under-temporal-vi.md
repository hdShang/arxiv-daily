---
layout: default
title: DIQ-H: Evaluating Hallucination Persistence in VLMs Under Temporal Visual Degradation
---

# DIQ-H: Evaluating Hallucination Persistence in VLMs Under Temporal Visual Degradation

**arXiv**: [2512.03992v1](https://arxiv.org/abs/2512.03992) | [PDF](https://arxiv.org/pdf/2512.03992.pdf)

**作者**: Zexin Lin, Hawen Wan, Yebin Zhong, Xiaoqiang

---

## 💡 一句话要点

**提出DIQ-H基准以评估视觉语言模型在时序视觉退化下的幻觉持续性**

**关键词**: `视觉语言模型` `时序视觉退化` `幻觉持续性` `基准评估` `鲁棒性测试` `多轮问答`

## 📋 核心要点

1. 现有基准忽略时序退化与错误传播，导致VLM在安全关键应用中存在关键失效模式
2. DIQ-H应用基于物理的视觉退化，通过多轮问答任务评估幻觉持续性、错误恢复和时序一致性
3. 实验显示16个先进VLM存在显著鲁棒性差距，GPT-4o恢复率仅78.5%，开源模型时序一致性低于60%

## 📄 摘要（原文）

> Vision-Language Models (VLMs) deployed in safety-critical applications such as autonomous driving must handle continuous visual streams under imperfect conditions. However, existing benchmarks focus on static, high-quality images and ignore temporal degradation and error propagation, which are critical failure modes where transient visual corruption induces hallucinations that persist across subsequent frames. We introduce DIQ-H, the first benchmark for evaluating VLM robustness under dynamic visual degradation in temporal sequences. DIQ-H applies physics-based corruptions including motion blur, sensor noise, and compression artifacts, and measures hallucination persistence, error recovery, and temporal consistency through multi-turn question-answering tasks. To enable scalable annotation, we propose Uncertainty-Guided Iterative Refinement (UIR), which generates reliable pseudo-ground-truth using lightweight VLMs with uncertainty filtering, achieving a 15.3 percent accuracy improvement. Experiments on 16 state-of-the-art VLMs reveal substantial robustness gaps: even advanced models such as GPT-4o achieve only a 78.5 percent recovery rate, while open-source models struggle with temporal consistency at less than 60 percent. DIQ-H provides a comprehensive platform for evaluating VLM reliability in real-world deployments.

