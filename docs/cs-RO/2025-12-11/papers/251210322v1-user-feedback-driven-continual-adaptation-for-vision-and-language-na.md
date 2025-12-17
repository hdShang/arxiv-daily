---
layout: default
title: User-Feedback-Driven Continual Adaptation for Vision-and-Language Navigation
---

# User-Feedback-Driven Continual Adaptation for Vision-and-Language Navigation

**arXiv**: [2512.10322v1](https://arxiv.org/abs/2512.10322) | [PDF](https://arxiv.org/pdf/2512.10322.pdf)

**作者**: Yongqiang Yu, Xuhui Li, Hazza Mahmood, Jinxing Zhou, Haodong Hong, Longtao Jiang, Zhiqiang Xu, Qi Wu, Xiaojun Chang

---

## 💡 一句话要点

**提出用户反馈驱动的持续适应框架，以增强视觉语言导航在真实部署中的性能。**

**关键词**: `视觉语言导航` `持续适应` `用户反馈` `记忆库热启动` `通用场景适应`

## 📋 核心要点

1. 核心问题：现有通用场景适应方法忽略用户反馈，依赖无监督适应，限制真实应用效果。
2. 方法要点：集成用户反馈（指令和纠正信号）生成高质量训练数据，结合记忆库热启动机制提升适应效率。
3. 实验或效果：在GSA-R2R基准上超越基线，提高导航成功率和路径效率，适应设置下表现稳健。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) requires agents to navigate complex environments by following natural-language instructions. General Scene Adaptation for VLN (GSA-VLN) shifts the focus from zero-shot generalization to continual, environment-specific adaptation, narrowing the gap between static benchmarks and real-world deployment. However, current GSA-VLN frameworks exclude user feedback, relying solely on unsupervised adaptation from repeated environmental exposure. In practice, user feedback offers natural and valuable supervision that can significantly enhance adaptation quality. We introduce a user-feedback-driven adaptation framework that extends GSA-VLN by systematically integrating human interactions into continual learning. Our approach converts user feedback-navigation instructions and corrective signals-into high-quality, environment-aligned training data, enabling efficient and realistic adaptation. A memory-bank warm-start mechanism further reuses previously acquired environmental knowledge, mitigating cold-start degradation and ensuring stable redeployment. Experiments on the GSA-R2R benchmark show that our method consistently surpasses strong baselines such as GR-DUET, improving navigation success and path efficiency. The memory-bank warm start stabilizes early navigation and reduces performance drops after updates. Results under both continual and hybrid adaptation settings confirm the robustness and generality of our framework, demonstrating sustained improvement across diverse deployment conditions.

