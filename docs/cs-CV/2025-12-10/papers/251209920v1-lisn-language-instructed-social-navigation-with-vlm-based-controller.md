---
layout: default
title: LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating
---

# LISN: Language-Instructed Social Navigation with VLM-based Controller Modulating

**arXiv**: [2512.09920v1](https://arxiv.org/abs/2512.09920) | [PDF](https://arxiv.org/pdf/2512.09920.pdf)

**作者**: Junting Chen, Yunchuan Li, Panfeng Jiang, Jiacheng Du, Zixuan Chen, Chenrui Tie, Jiajun Deng, Lin Shao

---

## 💡 一句话要点

**提出LISN-Bench基准与Social-Nav-Modulator系统，以解决语言指令社交导航问题。**

**关键词**: `社交导航` `语言指令` `视觉语言模型` `基准测试` `机器人控制` `动态避障`

## 📋 核心要点

1. 核心问题：现有社交导航研究主要关注路径效率和避障，缺乏对用户语言指令的遵循和场景理解。
2. 方法要点：采用基于VLM的快速-慢速分层系统，通过VLM代理调制成本图和控制器参数，解耦低级动作生成。
3. 实验或效果：在LISN-Bench上平均成功率91.3%，比最强基线提升超过63%，尤其在人群跟随和避禁区域任务中表现优异。

## 📄 摘要（原文）

> Towards human-robot coexistence, socially aware navigation is significant for mobile robots. Yet existing studies on this area focus mainly on path efficiency and pedestrian collision avoidance, which are essential but represent only a fraction of social navigation. Beyond these basics, robots must also comply with user instructions, aligning their actions to task goals and social norms expressed by humans. In this work, we present LISN-Bench, the first simulation-based benchmark for language-instructed social navigation. Built on Rosnav-Arena 3.0, it is the first standardized social navigation benchmark to incorporate instruction following and scene understanding across diverse contexts. To address this task, we further propose Social-Nav-Modulator, a fast-slow hierarchical system where a VLM agent modulates costmaps and controller parameters. Decoupling low-level action generation from the slower VLM loop reduces reliance on high-frequency VLM inference while improving dynamic avoidance and perception adaptability. Our method achieves an average success rate of 91.3%, which is greater than 63% than the most competitive baseline, with most of the improvements observed in challenging tasks such as following a person in a crowd and navigating while strictly avoiding instruction-forbidden regions. The project website is at: https://social-nav.github.io/LISN-project/

