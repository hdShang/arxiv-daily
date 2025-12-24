---
layout: default
title: "DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies"
---

# DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07813" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07813v1</a>
  <a href="https://arxiv.org/pdf/2505.07813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07813v1', 'DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tony Tao, Mohan Kumar Srirama, Jason Jingzhou Liu, Kenneth Shaw, Deepak Pathak

**分类**: cs.RO, cs.AI, cs.CV, cs.LG, eess.SY

**发布日期**: 2025-05-12

**备注**: In RSS 2025. Website at https://dexwild.github.io

---

## 💡 一句话要点

**提出DexWild以解决机器人数据收集的高成本问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `灵巧操作` `机器人学习` `数据收集` `联合训练` `泛化能力` `人机交互` `低成本设备`

## 📋 核心要点

1. 现有方法在获取大规模机器人数据集时面临高成本和可扩展性不足的问题。
2. DexWild通过让人类使用双手收集数据，结合人类与机器人演示的联合训练，提升了灵巧操作策略的泛化能力。
3. 实验结果显示，DexWild在未见环境中的成功率达到68.5%，显著优于仅使用机器人数据的策略。

## 📝 摘要（中文）

大规模、多样化的机器人数据集为灵巧操作策略在新环境中的泛化提供了可能，但获取这些数据集面临诸多挑战。尽管遥操作提供了高保真数据集，但其高成本限制了其可扩展性。DexWild通过让人们使用自己的手在多种环境和物体中收集数据，克服了这一限制。我们开发了DexWild-System，一个低成本、移动且易于使用的设备。DexWild学习框架在人工和机器人演示上进行联合训练，相比单独训练每个数据集，显著提高了性能。实验结果表明，DexWild在未见环境中的成功率达到68.5%，是仅使用机器人数据训练策略的近四倍，并且在跨体现泛化方面提升了5.8倍。

## 🔬 方法详解

**问题定义**：本论文旨在解决灵巧操作策略在新环境中的泛化能力不足，现有方法依赖于高成本的遥操作数据收集，限制了其可扩展性。

**核心思路**：DexWild的核心思路是通过人类自然的手部交互收集数据，利用DexWild-System设备进行数据记录，并在此基础上进行联合训练，以提升机器人策略的性能和泛化能力。

**技术框架**：DexWild的整体架构包括数据收集模块（DexWild-System）、数据处理模块和联合训练框架。数据收集模块由多样化的数据收集者使用手部交互进行数据采集，随后通过学习框架进行训练。

**关键创新**：DexWild的主要创新在于通过人类手部交互收集数据，并将人类与机器人演示进行联合训练，这种方法显著提高了策略在新环境中的成功率和泛化能力。

**关键设计**：在设计中，DexWild-System采用低成本的硬件配置，确保易于使用；联合训练过程中，采用特定的损失函数来平衡人类与机器人数据的贡献，以优化学习效果。

## 📊 实验亮点

实验结果显示，DexWild在未见环境中的成功率达到68.5%，是仅使用机器人数据训练策略的近四倍。此外，DexWild在跨体现泛化方面的表现提升了5.8倍，展示了其在灵巧操作领域的显著优势。

## 🎯 应用场景

DexWild的研究成果在多个领域具有潜在应用价值，如服务机器人、家庭自动化、工业机器人等。通过提高机器人在多样化环境中的操作能力，能够更好地满足人们的日常需求，推动智能机器人技术的普及与发展。

## 📄 摘要（原文）

> Large-scale, diverse robot datasets have emerged as a promising path toward enabling dexterous manipulation policies to generalize to novel environments, but acquiring such datasets presents many challenges. While teleoperation provides high-fidelity datasets, its high cost limits its scalability. Instead, what if people could use their own hands, just as they do in everyday life, to collect data? In DexWild, a diverse team of data collectors uses their hands to collect hours of interactions across a multitude of environments and objects. To record this data, we create DexWild-System, a low-cost, mobile, and easy-to-use device. The DexWild learning framework co-trains on both human and robot demonstrations, leading to improved performance compared to training on each dataset individually. This combination results in robust robot policies capable of generalizing to novel environments, tasks, and embodiments with minimal additional robot-specific data. Experimental results demonstrate that DexWild significantly improves performance, achieving a 68.5% success rate in unseen environments-nearly four times higher than policies trained with robot data only-and offering 5.8x better cross-embodiment generalization. Video results, codebases, and instructions at https://dexwild.github.io

