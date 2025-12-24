---
layout: default
title: Performance Guaranteed Poisoning Attacks in Federated Learning: A Sliding Mode Approach
---

# Performance Guaranteed Poisoning Attacks in Federated Learning: A Sliding Mode Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16403" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16403v2</a>
  <a href="https://arxiv.org/pdf/2505.16403.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16403v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16403v2', 'Performance Guaranteed Poisoning Attacks in Federated Learning: A Sliding Mode Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huazi Pan, Yanjun Zhang, Leo Yu Zhang, Scott Adams, Abbas Kouzani, Suiyang Khoo

**分类**: cs.LG, eess.SY

**发布日期**: 2025-05-22 (更新: 2025-05-29)

**备注**: This paper is to appear in IJCAI 2025, code available at: https://github.com/Halsey777/FedSA

---

## 💡 一句话要点

**提出滑模控制方法以解决联邦学习中的数据投毒攻击问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `联邦学习` `数据投毒` `滑模控制` `模型安全` `恶意攻击` `非线性控制` `机器学习`

## 📋 核心要点

1. 现有的投毒攻击方法多集中于导致服务拒绝，缺乏对全局模型准确率的精确控制。
2. 本文提出的FedSA方法利用滑模控制理论，能够以可控的方式引入投毒，精准降低全局模型的预测准确率。
3. 实验结果显示，FedSA在较少的恶意客户端下，能够实现预设的全局准确率，并保持隐蔽性和灵活的学习速率。

## 📝 摘要（中文）

在联邦学习（FL）中，局部训练数据和更新的操控，即数据投毒攻击，是一种主要威胁。现有的投毒攻击通常导致服务拒绝（DoS）问题。本文提出了一种新颖的攻击方法，称为联邦学习滑模攻击（FedSA），旨在以可控的方式精确引入投毒程度。FedSA结合了强健的非线性控制理论与模型投毒攻击，能够操控恶意客户端的更新，以控制的速率将全局模型驱向妥协状态。实验结果表明，FedSA能够在较少的恶意客户端下，准确实现预定义的全局准确率，同时保持高隐蔽性和可调的学习速率。

## 🔬 方法详解

**问题定义**：本文旨在解决联邦学习中的数据投毒攻击问题，现有方法往往导致全局模型的服务拒绝，而缺乏对模型准确率的精确操控。

**核心思路**：FedSA方法结合滑模控制理论，允许攻击者以可控的方式引入投毒，设定全局模型的准确率目标，从而实现对模型的精准操控。

**技术框架**：该方法的整体架构包括恶意客户端的更新操控、滑模控制的实施以及全局模型的反馈机制，确保攻击过程的隐蔽性和有效性。

**关键创新**：FedSA的主要创新在于将滑模控制理论应用于模型投毒攻击，允许攻击者在不显著影响学习过程的情况下，精确控制全局模型的准确率。

**关键设计**：在设计中，FedSA设置了预定义的目标准确率，并通过调整学习速率和控制参数，确保攻击的隐蔽性和有效性，同时减少所需的恶意客户端数量。

## 📊 实验亮点

实验结果表明，FedSA能够在仅有少量恶意客户端的情况下，成功将全局模型的准确率降低至预设目标，且在隐蔽性和学习速率的可调性方面表现优异，展示了其在攻击效果和效率上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括安全的联邦学习系统、分布式机器学习环境以及需要保护模型免受恶意攻击的场景。通过提高对投毒攻击的防御能力，能够增强联邦学习在实际应用中的可靠性和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Manipulation of local training data and local updates, i.e., the poisoning attack, is the main threat arising from the collaborative nature of the federated learning (FL) paradigm. Most existing poisoning attacks aim to manipulate local data/models in a way that causes denial-of-service (DoS) issues. In this paper, we introduce a novel attack method, named Federated Learning Sliding Attack (FedSA) scheme, aiming at precisely introducing the extent of poisoning in a subtle controlled manner. It operates with a predefined objective, such as reducing global model's prediction accuracy by 10%. FedSA integrates robust nonlinear control-Sliding Mode Control (SMC) theory with model poisoning attacks. It can manipulate the updates from malicious clients to drive the global model towards a compromised state, achieving this at a controlled and inconspicuous rate. Additionally, leveraging the robust control properties of FedSA allows precise control over the convergence bounds, enabling the attacker to set the global accuracy of the poisoned model to any desired level. Experimental results demonstrate that FedSA can accurately achieve a predefined global accuracy with fewer malicious clients while maintaining a high level of stealth and adjustable learning rates.

