---
layout: default
title: TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System
---

# TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System

**arXiv**: [2511.02832v1](https://arxiv.org/abs/2511.02832) | [PDF](https://arxiv.org/pdf/2511.02832.pdf)

**作者**: Yanjie Ze, Siheng Zhao, Weizhuo Wang, Angjoo Kanazawa, Rocky Duan, Pieter Abbeel, Guanya Shi, Jiajun Wu, C. Karen Liu

---

## 💡 一句话要点

**提出TWIST2系统以解决人形机器人数据收集的可扩展性和便携性问题**

**关键词**: `人形机器人` `全身控制` `自我中心视觉` `数据收集` `开源系统` `视觉运动策略`

## 📋 核心要点

1. 人形机器人缺乏高效数据收集框架，现有系统依赖昂贵动捕或解耦控制
2. TWIST2使用PICO4U VR和低成本机器人颈部实现全身控制与自我中心视觉
3. 系统在15分钟内收集100次演示，成功率近100%，并开源数据集和代码

## 📄 摘要（原文）

> Large-scale data has driven breakthroughs in robotics, from language models
> to vision-language-action models in bimanual manipulation. However, humanoid
> robotics lacks equally effective data collection frameworks. Existing humanoid
> teleoperation systems either use decoupled control or depend on expensive
> motion capture setups. We introduce TWIST2, a portable, mocap-free humanoid
> teleoperation and data collection system that preserves full whole-body control
> while advancing scalability. Our system leverages PICO4U VR for obtaining
> real-time whole-body human motions, with a custom 2-DoF robot neck (cost around
> $250) for egocentric vision, enabling holistic human-to-humanoid control. We
> demonstrate long-horizon dexterous and mobile humanoid skills and we can
> collect 100 demonstrations in 15 minutes with an almost 100% success rate.
> Building on this pipeline, we propose a hierarchical visuomotor policy
> framework that autonomously controls the full humanoid body based on egocentric
> vision. Our visuomotor policy successfully demonstrates whole-body dexterous
> manipulation and dynamic kicking tasks. The entire system is fully reproducible
> and open-sourced at https://yanjieze.com/TWIST2 . Our collected dataset is also
> open-sourced at https://twist-data.github.io .

