---
layout: default
title: RisConFix: LLM-based Automated Repair of Risk-Prone Drone Configurations
---

# RisConFix: LLM-based Automated Repair of Risk-Prone Drone Configurations

**arXiv**: [2512.07122v1](https://arxiv.org/abs/2512.07122) | [PDF](https://arxiv.org/pdf/2512.07122.pdf)

**作者**: Liping Han, Tingting Nie, Le Yu, Mingzhe Hu, Tao Yue

---

## 💡 一句话要点

**提出基于大语言模型的实时修复方法RisConFix，以解决无人机风险配置导致的飞行不稳定问题。**

**关键词**: `无人机配置修复` `大语言模型应用` `实时监控` `迭代修复` `飞行稳定性`

## 📋 核心要点

1. 无人机配置参数组合可能引发飞行不稳定，降低鲁棒性。
2. RisConFix利用LLM分析参数与状态关系，迭代生成修复更新。
3. 在ArduPilot案例中，修复成功率最高达97%，平均修复次数1.17。

## 📄 摘要（原文）

> Flight control software is typically designed with numerous configurable parameters governing multiple functionalities, enabling flexible adaptation to mission diversity and environmental uncertainty. Although developers and manufacturers usually provide recommendations for these parameters to ensure safe and stable operations, certain combinations of parameters with recommended values may still lead to unstable flight behaviors, thereby degrading the drone's robustness. To this end, we propose a Large Language Model (LLM) based approach for real-time repair of risk-prone configurations (named RisConFix) that degrade drone robustness. RisConFix continuously monitors the drone's operational state and automatically triggers a repair mechanism once abnormal flight behaviors are detected. The repair mechanism leverages an LLM to analyze relationships between configuration parameters and flight states, and then generates corrective parameter updates to restore flight stability. To ensure the validity of the updated configuration, RisConFix operates as an iterative process; it continuously monitors the drone's flight state and, if an anomaly persists after applying an update, automatically triggers the next repair cycle. We evaluated RisConFix through a case study of ArduPilot (with 1,421 groups of misconfigurations). Experimental results show that RisConFix achieved a best repair success rate of 97% and an optimal average number of repairs of 1.17, demonstrating its capability to effectively and efficiently repair risk-prone configurations in real time.

