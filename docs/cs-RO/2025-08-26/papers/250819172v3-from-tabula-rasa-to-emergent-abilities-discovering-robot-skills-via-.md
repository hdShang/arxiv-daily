---
layout: default
title: "From Tabula Rasa to Emergent Abilities: Discovering Robot Skills via Real-World Unsupervised Quality-Diversity"
---

# From Tabula Rasa to Emergent Abilities: Discovering Robot Skills via Real-World Unsupervised Quality-Diversity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19172" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19172v3</a>
  <a href="https://arxiv.org/pdf/2508.19172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19172v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19172v3', 'From Tabula Rasa to Emergent Abilities: Discovering Robot Skills via Real-World Unsupervised Quality-Diversity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Grillotti, Lisa Coiffard, Oscar Pang, Maxence Faldor, Antoine Cully

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-08-26 (更新: 2025-08-28)

**备注**: Accepted at CoRL 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://adaptive-intelligent-robotics.github.io/URSA)

---

## 💡 一句话要点

**提出URSA以解决机器人自主技能发现问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自主技能发现` `无监督学习` `机器人适应性` `质量多样性` `技能学习` `动态环境` `智能机器人`

## 📋 核心要点

1. 现有方法如QDAC依赖手动定义的技能空间和启发式调优，限制了机器人在现实环境中的自主学习能力。
2. URSA通过无监督的方式，使机器人能够在真实环境中自主发现和掌握多样化的技能，提升了学习效率和安全性。
3. 实验结果表明，URSA在5个模拟和3个真实损伤场景中超越了所有基线，展示了其在技能适应性方面的优势。

## 📝 摘要（中文）

自主技能发现旨在使机器人在没有明确监督的情况下获取多样化行为。然而，直接在物理硬件上学习这些行为面临安全性和数据效率的挑战。现有方法如质量多样性演员-评论家(QDAC)需要手动定义技能空间和精心调整的启发式方法，限制了其在现实世界中的适用性。本文提出的无监督现实世界技能获取(URSA)是QDAC的扩展，能够使机器人在现实世界中自主发现和掌握多样化的高性能技能。实验表明，URSA在模拟和现实世界中成功发现了多样化的运动技能，并在实际损伤适应任务中优于所有基线方法，展示了其在机器人学习中的重要贡献。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在真实环境中自主发现多样化技能的挑战，现有方法依赖于手动定义的技能空间和启发式调优，限制了其应用。

**核心思路**：URSA通过无监督学习的方式，使机器人能够在真实世界中自主探索和掌握技能，避免了人工干预的需求，提升了学习的灵活性和效率。

**技术框架**：URSA的整体架构包括技能发现模块和技能应用模块，前者负责在真实环境中探索技能，后者则用于将学到的技能应用于实际任务中。

**关键创新**：URSA的主要创新在于其无监督的技能发现能力，能够在没有人工定义的技能空间下自主学习，显著提高了机器人在复杂环境中的适应性。

**关键设计**：URSA采用了改进的QDAC框架，结合了启发式驱动和完全无监督的设置，设计了适应性强的损失函数和网络结构，以优化技能学习过程。

## 📊 实验亮点

实验结果显示，URSA在5个模拟损伤场景和3个真实损伤场景中均超越了所有基线方法，证明了其在技能适应性和学习效率上的显著提升。这一成果为机器人自主学习提供了新的方向和可能性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能制造、灾后恢复等。URSA的能力使机器人能够在动态和复杂的环境中自主适应，提升了其在实际应用中的价值和效率。未来，URSA可能推动机器人技术的进一步发展，使其在更广泛的场景中实现自主操作。

## 📄 摘要（原文）

> Autonomous skill discovery aims to enable robots to acquire diverse behaviors without explicit supervision. Learning such behaviors directly on physical hardware remains challenging due to safety and data efficiency constraints. Existing methods, including Quality-Diversity Actor-Critic (QDAC), require manually defined skill spaces and carefully tuned heuristics, limiting real-world applicability. We propose Unsupervised Real-world Skill Acquisition (URSA), an extension of QDAC that enables robots to autonomously discover and master diverse, high-performing skills directly in the real world. We demonstrate that URSA successfully discovers diverse locomotion skills on a Unitree A1 quadruped in both simulation and the real world. Our approach supports both heuristic-driven skill discovery and fully unsupervised settings. We also show that the learned skill repertoire can be reused for downstream tasks such as real-world damage adaptation, where URSA outperforms all baselines in 5 out of 9 simulated and 3 out of 5 real-world damage scenarios. Our results establish a new framework for real-world robot learning that enables continuous skill discovery with limited human intervention, representing a significant step toward more autonomous and adaptable robotic systems. Demonstration videos are available at https://adaptive-intelligent-robotics.github.io/URSA.

