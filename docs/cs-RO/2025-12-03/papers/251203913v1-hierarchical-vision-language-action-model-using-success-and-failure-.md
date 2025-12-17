---
layout: default
title: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations
---

# Hierarchical Vision Language Action Model Using Success and Failure Demonstrations

**arXiv**: [2512.03913v1](https://arxiv.org/abs/2512.03913) | [PDF](https://arxiv.org/pdf/2512.03913.pdf)

**作者**: Jeongeun Park, Jihwan Yoon, Byungwoo Jeon, Juhan Park, Jinwoo Shin, Namhoon Cho, Kyungjae Lee, Sangdoo Yun, Sungjoon Choi

---

## 💡 一句话要点

**提出VINE分层视觉语言动作模型，利用失败演示提升机器人操作鲁棒性**

**关键词**: `视觉语言动作模型` `分层强化学习` `失败数据利用` `机器人操作` `离线训练` `鲁棒性提升`

## 📋 核心要点

1. 问题：现有VLA模型仅用成功演示训练，忽略失败数据中的脆弱性信息
2. 方法：分层强化学习框架，System 2进行可行性树搜索，System 1执行底层控制
3. 效果：在离线数据训练下，提高任务成功率和鲁棒性，验证失败数据价值

## 📄 摘要（原文）

> Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

