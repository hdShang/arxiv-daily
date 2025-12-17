---
layout: default
title: PHUMA: Physically-Grounded Humanoid Locomotion Dataset
---

# PHUMA: Physically-Grounded Humanoid Locomotion Dataset

**arXiv**: [2510.26236v1](https://arxiv.org/abs/2510.26236) | [PDF](https://arxiv.org/pdf/2510.26236.pdf)

**作者**: Kyungmin Lee, Sibeen Kim, Minho Park, Hyunseung Kim, Dongyoon Hwang, Hojoon Lee, Jaegul Choo

---

## 💡 一句话要点

**提出PHUMA数据集以解决人形机器人运动模仿中的物理伪影问题**

**关键词**: `人形机器人运动模仿` `物理约束重定向` `大规模视频数据集` `运动伪影消除` `路径跟随控制`

## 📋 核心要点

1. 现有运动捕捉数据集稀缺昂贵，网络视频转换引入物理伪影如漂浮和脚滑
2. PHUMA通过大规模人类视频、数据筛选和物理约束重定向消除伪影
3. 在未见运动模仿和路径跟随实验中，PHUMA训练策略优于Humanoid-X和AMASS

## 📄 摘要（原文）

> Motion imitation is a promising approach for humanoid locomotion, enabling
> agents to acquire humanlike behaviors. Existing methods typically rely on
> high-quality motion capture datasets such as AMASS, but these are scarce and
> expensive, limiting scalability and diversity. Recent studies attempt to scale
> data collection by converting large-scale internet videos, exemplified by
> Humanoid-X. However, they often introduce physical artifacts such as floating,
> penetration, and foot skating, which hinder stable imitation. In response, we
> introduce PHUMA, a Physically-grounded HUMAnoid locomotion dataset that
> leverages human video at scale, while addressing physical artifacts through
> careful data curation and physics-constrained retargeting. PHUMA enforces joint
> limits, ensures ground contact, and eliminates foot skating, producing motions
> that are both large-scale and physically reliable. We evaluated PHUMA in two
> sets of conditions: (i) imitation of unseen motion from self-recorded test
> videos and (ii) path following with pelvis-only guidance. In both cases,
> PHUMA-trained policies outperform Humanoid-X and AMASS, achieving significant
> gains in imitating diverse motions. The code is available at
> https://davian-robotics.github.io/PHUMA.

