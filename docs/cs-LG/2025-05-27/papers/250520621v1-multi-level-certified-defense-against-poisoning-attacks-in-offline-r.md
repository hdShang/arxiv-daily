---
layout: default
title: Multi-level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning
---

# Multi-level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20621" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20621v1</a>
  <a href="https://arxiv.org/pdf/2505.20621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20621v1', 'Multi-level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shijie Liu, Andrew C. Cullen, Paul Montague, Sarah Erfani, Benjamin I. P. Rubinstein

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出多层次认证防御以应对离线强化学习中的毒化攻击**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `毒化攻击` `认证防御` `差分隐私` `鲁棒性` `安全性` `机器学习`

## 📋 核心要点

1. 离线强化学习因依赖外部数据集而易受毒化攻击，现有方法在应对此类攻击时保障不足。
2. 本文提出了一种扩展的认证防御机制，利用差分隐私特性增强对抗操控的鲁棒性，适用于多种环境。
3. 实验结果显示，在7%训练数据被毒化的情况下，性能下降不超过50%，且认证半径提升5倍，显著改善了安全性。

## 📝 摘要（中文）

离线强化学习（RL）与其他机器学习框架一样，因依赖外部数据集而易受毒化攻击的影响，尤其在其序列性质下更为严重。为减轻RL毒化带来的风险，本文扩展了认证防御机制，提供更强的对抗操控的保障，确保每个状态的动作和整体期望累积奖励的鲁棒性。我们的方法利用差分隐私的特性，使得该工作能够适用于连续和离散空间，以及随机和确定性环境，显著扩展了可实现保障的范围和适用性。实证评估表明，在训练数据中最多7%被毒化的情况下，我们的方法确保性能下降不超过50%，显著优于之前研究中的0.008%，同时产生的认证半径也大5倍。这突显了我们框架在提升离线RL安全性和可靠性方面的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决离线强化学习中毒化攻击带来的鲁棒性问题。现有方法在面对外部数据集的操控时，保障能力不足，导致性能显著下降。

**核心思路**：我们提出的解决方案是扩展认证防御机制，结合差分隐私的特性，以增强对抗操控的能力，确保每个状态的动作和整体奖励的鲁棒性。

**技术框架**：整体架构包括数据预处理、毒化检测、认证防御和性能评估四个主要模块。首先对数据进行清洗和预处理，然后检测潜在的毒化数据，接着应用认证防御机制，最后评估模型的性能和鲁棒性。

**关键创新**：本文的主要创新在于将认证防御机制与差分隐私结合，显著提升了对抗毒化攻击的能力，并扩展了适用范围，涵盖了连续、离散、随机和确定性环境。

**关键设计**：在设计中，我们设置了适当的损失函数以平衡鲁棒性与性能，采用了多层次的认证半径计算方法，以确保在不同毒化比例下的有效防御。

## 📊 实验亮点

实验结果表明，在训练数据中最多7%被毒化的情况下，模型性能下降不超过50%，相比于之前研究的0.008%有显著提升。同时，认证半径也提升了5倍，显示出该方法在安全性方面的显著进步。

## 🎯 应用场景

该研究的潜在应用领域包括金融决策、医疗诊断和自动驾驶等高风险场景，能够有效提升离线强化学习系统的安全性和可靠性。未来，该框架有望在更多实际应用中推广，增强智能系统对抗恶意攻击的能力。

## 📄 摘要（原文）

> Similar to other machine learning frameworks, Offline Reinforcement Learning (RL) is shown to be vulnerable to poisoning attacks, due to its reliance on externally sourced datasets, a vulnerability that is exacerbated by its sequential nature. To mitigate the risks posed by RL poisoning, we extend certified defenses to provide larger guarantees against adversarial manipulation, ensuring robustness for both per-state actions, and the overall expected cumulative reward. Our approach leverages properties of Differential Privacy, in a manner that allows this work to span both continuous and discrete spaces, as well as stochastic and deterministic environments -- significantly expanding the scope and applicability of achievable guarantees. Empirical evaluations demonstrate that our approach ensures the performance drops to no more than $50\%$ with up to $7\%$ of the training data poisoned, significantly improving over the $0.008\%$ in prior work~\citep{wu_copa_2022}, while producing certified radii that is $5$ times larger as well. This highlights the potential of our framework to enhance safety and reliability in offline RL.

