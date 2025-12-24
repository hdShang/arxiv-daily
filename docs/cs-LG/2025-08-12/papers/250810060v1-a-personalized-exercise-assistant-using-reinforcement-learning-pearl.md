---
layout: default
title: "A Personalized Exercise Assistant using Reinforcement Learning (PEARL): Results from a four-arm Randomized-controlled Trial"
---

# A Personalized Exercise Assistant using Reinforcement Learning (PEARL): Results from a four-arm Randomized-controlled Trial

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10060" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10060v1</a>
  <a href="https://arxiv.org/pdf/2508.10060.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10060v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10060v1', 'A Personalized Exercise Assistant using Reinforcement Learning (PEARL): Results from a four-arm Randomized-controlled Trial')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amy Armento Lee, Narayan Hegde, Nina Deliu, Emily Rosenzweig, Arun Suggala, Sriram Lakshminarasimhan, Qian He, John Hernandez, Martin Seneviratne, Rahul Singh, Pradnesh Kalkar, Karthikeyan Shanmugam, Aravindan Raghuveer, Abhimanyu Singh, My Nguyen, James Taylor, Jatin Alla, Sofia S. Villar, Hulya Emir-Farinas

**分类**: cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出个性化运动助手PEARL以解决身体活动不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `个性化干预` `强化学习` `身体活动` `移动健康` `行为科学` `随机对照试验` `健康促进`

## 📋 核心要点

1. 现有的身体活动促进方法缺乏个性化，难以有效激励用户持续运动。
2. 本研究提出了一种基于强化学习的个性化运动助手，通过分析用户行为数据动态调整运动提示。
3. 实验结果显示，RL组在1个月和2个月内的日均步数显著高于对照组，证明了该方法的有效性。

## 📝 摘要（中文）

身体不活动是全球健康面临的重大挑战。移动健康干预，尤其是及时适应性干预（JITAIs），为可扩展的个性化身体活动促进提供了有前景的途径。然而，在大规模开发和评估这些干预措施时，结合稳健的行为科学面临方法论障碍。PEARL研究是首个大规模的四臂随机对照试验，评估了一种基于强化学习（RL）算法的干预，旨在通过Fitbit应用个性化身体活动提示。研究共招募了13,463名Fitbit用户，结果显示RL组在身体活动方面显著优于其他组，表明基于行为科学的RL方法在数字健康干预中的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决身体活动不足的问题，现有方法往往缺乏个性化，难以满足不同用户的需求，导致干预效果不佳。

**核心思路**：本研究提出了一种基于强化学习的个性化运动助手PEARL，通过分析用户的行为数据，动态调整运动提示的内容和时机，以提高用户的身体活动水平。

**技术框架**：研究设计为四臂随机对照试验，包含对照组、随机组、固定组和RL组。RL组使用强化学习算法选择提示，其他组则采用不同的提示选择策略。

**关键创新**：本研究的主要创新在于将强化学习算法应用于个性化健康干预，利用用户的实时反馈优化提示策略，与传统的静态或随机提示方法相比，能够更有效地激励用户。

**关键设计**：研究中使用了155条基于行为科学原则的运动提示，RL算法根据用户的反馈和行为数据进行动态调整，确保提示的个性化和时效性。

## 📊 实验亮点

实验结果显示，RL组在1个月内的日均步数较对照组增加296步，较随机组增加218步，较固定组增加238步；在2个月时，RL组仍保持较对照组增加210步的显著提升，表明该方法在促进身体活动方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括移动健康应用、个性化健身指导以及公共健康干预等。通过个性化的运动提示，能够有效提高用户的身体活动水平，改善健康状况，具有重要的社会价值和实际意义。未来，该方法还可以扩展到其他健康行为的促进，如饮食管理和心理健康干预等。

## 📄 摘要（原文）

> Consistent physical inactivity poses a major global health challenge. Mobile health (mHealth) interventions, particularly Just-in-Time Adaptive Interventions (JITAIs), offer a promising avenue for scalable, personalized physical activity (PA) promotion. However, developing and evaluating such interventions at scale, while integrating robust behavioral science, presents methodological hurdles. The PEARL study was the first large-scale, four-arm randomized controlled trial to assess a reinforcement learning (RL) algorithm, informed by health behavior change theory, to personalize the content and timing of PA nudges via a Fitbit app.
>   We enrolled and randomized 13,463 Fitbit users into four study arms: control, random, fixed, and RL. The control arm received no nudges. The other three arms received nudges from a bank of 155 nudges based on behavioral science principles. The random arm received nudges selected at random. The fixed arm received nudges based on a pre-set logic from survey responses about PA barriers. The RL group received nudges selected by an adaptive RL algorithm. We included 7,711 participants in primary analyses (mean age 42.1, 86.3% female, baseline steps 5,618.2).
>   We observed an increase in PA for the RL group compared to all other groups from baseline to 1 and 2 months. The RL group had significantly increased average daily step count at 1 month compared to all other groups: control (+296 steps, p=0.0002), random (+218 steps, p=0.005), and fixed (+238 steps, p=0.002). At 2 months, the RL group sustained a significant increase compared to the control group (+210 steps, p=0.0122). Generalized estimating equation models also revealed a sustained increase in daily steps in the RL group vs. control (+208 steps, p=0.002). These findings demonstrate the potential of a scalable, behaviorally-informed RL approach to personalize digital health interventions for PA.

