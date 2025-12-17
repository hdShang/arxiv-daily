---
layout: default
title: $π^{*}_{0.6}$: a VLA That Learns From Experience
---

# $π^{*}_{0.6}$: a VLA That Learns From Experience

**arXiv**: [2511.14759v1](https://arxiv.org/abs/2511.14759) | [PDF](https://arxiv.org/pdf/2511.14759.pdf)

**作者**: Ali Amin, Raichelle Aniceto, Ashwin Balakrishna, Kevin Black, Ken Conley, Grace Connors, James Darpinian, Karan Dhabalia, Jared DiCarlo, Danny Driess, Michael Equi, Adnan Esmail, Yunhao Fang, Chelsea Finn, Catherine Glossop, Thomas Godden, Ivan Goryachev, Lachy Groom, Hunter Hancock, Karol Hausman, Gashon Hussein, Brian Ichter, Szymon Jakubczak, Rowan Jen, Tim Jones, Ben Katz, Liyiming Ke, Chandra Kuchi, Marinda Lamb, Devin LeBlanc, Sergey Levine, Adrian Li-Bell, Yao Lu, Vishnu Mano, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Allen Z. Ren, Charvi Sharma, Lucy Xiaoyang Shi, Laura Smith, Jost Tobias Springenberg, Kyle Stachowicz, Will Stoeckle, Alex Swerdlow, James Tanner, Marcel Torne, Quan Vuong, Anna Walling, Haohuan Wang, Blake Williams, Sukwon Yoo, Lili Yu, Ury Zhilinsky, Zhiyuan Zhou

---

## 💡 一句话要点

**提出RECAP方法，通过强化学习提升视觉-语言-动作模型在真实任务中的性能。**

**关键词**: `视觉-语言-动作模型` `强化学习` `机器人学习` `异构数据整合` `真实世界部署`

## 📋 核心要点

1. 研究视觉-语言-动作模型如何通过真实部署和强化学习实现自我改进。
2. RECAP方法整合异构数据，包括演示、在线收集和专家干预，进行优势条件策略训练。
3. 实验显示，RECAP在叠衣物、组装箱子和制作咖啡等任务中显著提升吞吐量和降低失败率。

## 📄 摘要（原文）

> We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

