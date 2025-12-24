---
layout: default
title: "MetaCipher: A Time-Persistent and Universal Multi-Agent Framework for Cipher-Based Jailbreak Attacks for LLMs"
---

# MetaCipher: A Time-Persistent and Universal Multi-Agent Framework for Cipher-Based Jailbreak Attacks for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22557" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22557v2</a>
  <a href="https://arxiv.org/pdf/2506.22557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22557v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22557v2', 'MetaCipher: A Time-Persistent and Universal Multi-Agent Framework for Cipher-Based Jailbreak Attacks for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyuan Chen, Minghao Shao, Abdul Basit, Siddharth Garg, Muhammad Shafique

**分类**: cs.CR, cs.LG

**发布日期**: 2025-06-27 (更新: 2025-08-13)

---

## 💡 一句话要点

**提出MetaCipher以解决LLMs的低成本多代理越狱攻击问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越狱攻击` `大型语言模型` `强化学习` `多代理系统` `安全性评估`

## 📋 核心要点

1. 现有越狱攻击方法面临高查询成本和攻击有效性短暂的问题，限制了研究的成本效益和实际影响。
2. MetaCipher是一个低成本的多代理越狱框架，利用强化学习实现模块化和自适应，能够适应不同的LLMs。
3. 在多种受害模型和基准上进行的大规模评估显示，MetaCipher在攻击成功率上优于以往方法，表现出良好的鲁棒性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）能力的提升，它们面临越来越复杂的越狱攻击威胁。尽管开发者在对齐微调和安全防护上投入巨大，研究者们仍在不断提出新型攻击，推动对抗性迭代的发展。然而，现有越狱攻击面临两个主要挑战：查询顶级LLMs的高成本和有效攻击的短暂生命周期。为了解决这些问题，本文提出了MetaCipher，一个低成本的多代理越狱框架，能够在不同安全措施的LLMs之间进行泛化。通过强化学习，MetaCipher具有模块化和自适应性，支持未来策略的扩展。在仅需10次查询的情况下，MetaCipher在最新的恶意提示基准上实现了最先进的攻击成功率，超越了以往的越狱方法。我们进行了大规模的实证评估，展示了其鲁棒性和适应性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在面对越狱攻击时的高成本和短效性问题。现有方法在查询顶级模型时成本高昂，且由于频繁的安全更新，攻击的有效性往往很短暂。

**核心思路**：MetaCipher通过构建一个低成本的多代理框架，利用强化学习实现模块化和自适应，能够在不同的LLMs上泛化，支持未来策略的扩展。这样的设计旨在提高攻击的成本效益和持久性。

**技术框架**：MetaCipher的整体架构包括多个代理，每个代理负责生成和优化攻击策略。框架通过强化学习算法进行训练，支持在不同的安全措施下进行有效的越狱攻击。

**关键创新**：MetaCipher的主要创新在于其低成本和多代理设计，使其能够在短时间内实现高成功率的越狱攻击。这与传统方法相比，显著提高了攻击的效率和适应性。

**关键设计**：在技术细节上，MetaCipher采用了特定的损失函数和网络结构，以优化代理的学习过程。此外，框架的模块化设计使得未来的策略扩展变得更加灵活和高效。

## 📊 实验亮点

MetaCipher在仅需10次查询的情况下，达到了最新恶意提示基准上的最先进攻击成功率，显著超越了以往的越狱方法，展示了其在多种受害模型上的鲁棒性和适应性。

## 🎯 应用场景

MetaCipher的研究成果在安全领域具有广泛的应用潜力，尤其是在对抗性攻击和模型安全性评估方面。其低成本和高效的特性使得研究者和开发者能够更有效地测试和提升大型语言模型的安全性，未来可能推动更安全的AI系统的开发。

## 📄 摘要（原文）

> As large language models (LLMs) grow more capable, they face growing vulnerability to sophisticated jailbreak attacks. While developers invest heavily in alignment finetuning and safety guardrails, researchers continue publishing novel attacks, driving progress through adversarial iteration. This dynamic mirrors a strategic game of continual evolution. However, two major challenges hinder jailbreak development: the high cost of querying top-tier LLMs and the short lifespan of effective attacks due to frequent safety updates. These factors limit cost-efficiency and practical impact of research in jailbreak attacks. To address this, we propose MetaCipher, a low-cost, multi-agent jailbreak framework that generalizes across LLMs with varying safety measures. Using reinforcement learning, MetaCipher is modular and adaptive, supporting extensibility to future strategies. Within as few as 10 queries, MetaCipher achieves state-of-the-art attack success rates on recent malicious prompt benchmarks, outperforming prior jailbreak methods. We conduct a large-scale empirical evaluation across diverse victim models and benchmarks, demonstrating its robustness and adaptability. Warning: This paper contains model outputs that may be offensive or harmful, shown solely to demonstrate jailbreak efficacy.

