---
layout: default
title: Practical Adversarial Attacks on Stochastic Bandits via Fake Data Injection
---

# Practical Adversarial Attacks on Stochastic Bandits via Fake Data Injection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21938" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21938v2</a>
  <a href="https://arxiv.org/pdf/2505.21938.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21938v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21938v2', 'Practical Adversarial Attacks on Stochastic Bandits via Fake Data Injection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qirun Zeng, Eric He, Richard Hoffmann, Xuchuang Wang, Jinhang Zuo

**分类**: cs.LG, cs.AI, cs.CR

**发布日期**: 2025-05-28 (更新: 2025-05-31)

---

## 💡 一句话要点

**提出假数据注入模型以解决随机带宽的对抗攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `对抗攻击` `随机带宽` `假数据注入` `机器学习` `算法安全`

## 📋 核心要点

1. 现有的对抗攻击方法通常依赖于不切实际的假设，限制了其在真实世界中的应用。
2. 本文提出假数据注入模型，允许攻击者在有限的约束下注入假反馈，模拟合法交互。
3. 实验结果表明，所提策略在多轮中有效误导了主流算法，显示出显著的脆弱性。

## 📝 摘要（中文）

对随机带宽的对抗攻击传统上依赖于一些不切实际的假设，例如每轮奖励操控和无限扰动，这限制了其在现实系统中的相关性。本文提出了一种更为实际的威胁模型——假数据注入，反映了现实对抗约束：攻击者只能将有限数量的有界假反馈样本注入学习者的历史中，以模拟合法交互。我们在此模型下设计了高效的攻击策略，明确解决了奖励值的幅度约束和数据注入的时间约束。理论分析表明，这些攻击可以在几乎所有轮次中误导上置信界（UCB）和汤普森采样算法选择目标臂，同时仅需付出次线性攻击成本。对合成和真实数据集的实验验证了我们策略的有效性，揭示了广泛使用的随机带宽算法在实际对抗场景下的显著脆弱性。

## 🔬 方法详解

**问题定义**：本文解决的是随机带宽算法在面对对抗攻击时的脆弱性问题。现有方法通常假设攻击者可以无限制地操控奖励，这在实际应用中并不现实。

**核心思路**：论文提出的假数据注入模型允许攻击者在有限的时间和幅度内注入假反馈，从而更真实地模拟对抗场景。通过这种方式，攻击者可以有效地误导学习算法。

**技术框架**：整体架构包括攻击策略设计、理论分析和实验验证三个主要模块。攻击策略设计中考虑了奖励值和时间的约束，理论分析则验证了攻击的有效性，最后通过实验验证了策略在真实数据集上的表现。

**关键创新**：最重要的技术创新在于提出了假数据注入这一新模型，突破了传统方法对攻击者能力的限制，使得攻击更加贴近实际应用场景。

**关键设计**：在设计中，设置了攻击的幅度和时间约束，确保攻击者的行为在可接受范围内。同时，采用了理论分析方法来评估攻击的效果，确保了策略的有效性和实用性。

## 📊 实验亮点

实验结果显示，所提攻击策略在多轮中能够有效误导UCB和汤普森采样算法，攻击成本仅为次线性，且在合成和真实数据集上均表现出显著的效果，揭示了随机带宽算法的脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括在线推荐系统、广告投放和动态定价等场景。在这些领域中，攻击者可能通过注入假数据来操控系统决策，从而影响用户体验和商业利益。未来，该研究有助于提升算法的鲁棒性，减少对抗攻击的影响。

## 📄 摘要（原文）

> Adversarial attacks on stochastic bandits have traditionally relied on some unrealistic assumptions, such as per-round reward manipulation and unbounded perturbations, limiting their relevance to real-world systems. We propose a more practical threat model, Fake Data Injection, which reflects realistic adversarial constraints: the attacker can inject only a limited number of bounded fake feedback samples into the learner's history, simulating legitimate interactions. We design efficient attack strategies under this model, explicitly addressing both magnitude constraints (on reward values) and temporal constraints (on when and how often data can be injected). Our theoretical analysis shows that these attacks can mislead both Upper Confidence Bound (UCB) and Thompson Sampling algorithms into selecting a target arm in nearly all rounds while incurring only sublinear attack cost. Experiments on synthetic and real-world datasets validate the effectiveness of our strategies, revealing significant vulnerabilities in widely used stochastic bandit algorithms under practical adversarial scenarios.

