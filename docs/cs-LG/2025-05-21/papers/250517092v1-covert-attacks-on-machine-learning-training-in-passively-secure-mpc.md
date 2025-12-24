---
layout: default
title: Covert Attacks on Machine Learning Training in Passively Secure MPC
---

# Covert Attacks on Machine Learning Training in Passively Secure MPC

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17092" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17092v1</a>
  <a href="https://arxiv.org/pdf/2505.17092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17092v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17092v1', 'Covert Attacks on Machine Learning Training in Passively Secure MPC')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matthew Jagielski, Daniel Escudero, Rahul Rachuri, Peter Scholl

**分类**: cs.CR, cs.LG

**发布日期**: 2025-05-21

---

## 💡 一句话要点

**提出有效攻击以揭示被动安全MPC训练中的隐患**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `安全多方计算` `机器学习` `隐私保护` `主动安全协议` `数据重构` `模型完整性` `攻击模型`

## 📋 核心要点

1. 现有的被动安全MPC训练协议未能有效防范主动对手的攻击，导致模型的完整性和隐私性受到威胁。
2. 论文提出了一种简单有效的攻击方法，主动对手可以在不被检测的情况下破坏MPC训练过程，重构训练数据。
3. 实验结果表明，所提出的攻击能够成功地影响模型的训练，显示出被动安全协议的脆弱性，呼吁使用更安全的主动协议。

## 📝 摘要（中文）

安全多方计算（MPC）允许数据拥有者在保持训练数据私密的情况下，基于联合数据训练机器学习模型。现有的MPC威胁模型考虑了被动腐败的对手，但本研究展示了主动对手可以在被动安全的MPC训练协议中实施的有效攻击，这些攻击几乎没有被检测到的风险。这些攻击不仅危及模型的完整性，还可能重构出精确的训练数据。研究结果挑战了在隐私保护机器学习（PPML）背景下，认为不包含恶意行为的威胁模型是合理的观点，强调了使用主动安全协议进行训练的必要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决被动安全的MPC训练协议在面对主动对手时的脆弱性。现有方法未能考虑恶意行为，导致模型的隐私和完整性受到威胁。

**核心思路**：论文的核心思路是展示主动对手如何在被动安全的MPC协议中实施攻击，利用协议设计的漏洞进行数据重构和模型操控。通过这种方式，研究者揭示了现有安全模型的不足。

**技术框架**：整体架构包括攻击模型的设计、攻击实施的步骤以及对模型完整性和隐私性的评估。主要模块包括攻击者模型、被攻击的MPC协议以及评估机制。

**关键创新**：最重要的技术创新在于提出了具体的攻击策略，能够在不被检测的情况下有效破坏MPC训练过程。这与现有方法的本质区别在于，现有方法通常假设参与方是诚实的，而本研究则揭示了这一假设的脆弱性。

**关键设计**：关键设计包括对攻击参数的选择、攻击实施的时机以及对MPC协议的具体操作细节。这些设计确保了攻击的隐蔽性和有效性。具体的损失函数和评估指标也被精心设计，以便准确评估攻击效果。

## 📊 实验亮点

实验结果显示，提出的攻击方法能够在不被检测的情况下成功重构训练数据，影响模型的训练效果。与传统被动安全协议相比，攻击成功率显著提高，表明现有协议在面对主动对手时的脆弱性。

## 🎯 应用场景

该研究的潜在应用场景包括金融数据分析、医疗数据共享以及其他需要保护隐私的多方计算环境。通过揭示被动安全MPC的脆弱性，促使研究者和开发者在实际应用中采用更为安全的主动安全协议，从而提高数据隐私保护的有效性。

## 📄 摘要（原文）

> Secure multiparty computation (MPC) allows data owners to train machine learning models on combined data while keeping the underlying training data private. The MPC threat model either considers an adversary who passively corrupts some parties without affecting their overall behavior, or an adversary who actively modifies the behavior of corrupt parties. It has been argued that in some settings, active security is not a major concern, partly because of the potential risk of reputation loss if a party is detected cheating.
>   In this work we show explicit, simple, and effective attacks that an active adversary can run on existing passively secure MPC training protocols, while keeping essentially zero risk of the attack being detected. The attacks we show can compromise both the integrity and privacy of the model, including attacks reconstructing exact training data. Our results challenge the belief that a threat model that does not include malicious behavior by the involved parties may be reasonable in the context of PPML, motivating the use of actively secure protocols for training.

