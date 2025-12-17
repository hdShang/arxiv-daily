---
layout: default
title: Dataset Poisoning Attacks on Behavioral Cloning Policies
---

# Dataset Poisoning Attacks on Behavioral Cloning Policies

**arXiv**: [2511.20992v1](https://arxiv.org/abs/2511.20992) | [PDF](https://arxiv.org/pdf/2511.20992.pdf)

**作者**: Akansha Kalra, Soumil Datta, Ethan Gilmore, Duc La, Guanhong Tao, Daniel S. Brown

---

## 💡 一句话要点

**提出行为克隆策略的清洁标签后门攻击，评估其在真实部署中的脆弱性。**

**关键词**: `行为克隆` `数据集污染` `后门攻击` `视觉触发器` `策略脆弱性`

## 📋 核心要点

1. 核心问题：行为克隆策略在真实世界部署中面临后门攻击的脆弱性。
2. 方法要点：通过注入视觉触发器污染数据集，并引入基于熵的测试时攻击。
3. 实验或效果：即使少量污染数据，策略在部署时性能显著下降。

## 📄 摘要（原文）

> Behavior Cloning (BC) is a popular framework for training sequential decision policies from expert demonstrations via supervised learning. As these policies are increasingly being deployed in the real world, their robustness and potential vulnerabilities are an important concern. In this work, we perform the first analysis of the efficacy of clean-label backdoor attacks on BC policies. Our backdoor attacks poison a dataset of demonstrations by injecting a visual trigger to create a spurious correlation that can be exploited at test time. We evaluate how policy vulnerability scales with the fraction of poisoned data, the strength of the trigger, and the trigger type. We also introduce a novel entropy-based test-time trigger attack that substantially degrades policy performance by identifying critical states where test-time triggering of the backdoor is expected to be most effective at degrading performance. We empirically demonstrate that BC policies trained on even minimally poisoned datasets exhibit deceptively high, near-baseline task performance despite being highly vulnerable to backdoor trigger attacks during deployment. Our results underscore the urgent need for more research into the robustness of BC policies, particularly as large-scale datasets are increasingly used to train policies for real-world cyber-physical systems. Videos and code are available at https://sites.google.com/view/dataset-poisoning-in-bc.

