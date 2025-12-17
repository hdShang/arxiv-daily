---
layout: default
title: SCOOP'D: Learning Mixed-Liquid-Solid Scooping via Sim2Real Generative Policy
---

# SCOOP'D: Learning Mixed-Liquid-Solid Scooping via Sim2Real Generative Policy

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11566" target="_blank" class="toolbar-btn">arXiv: 2510.11566v1</a>
    <a href="https://arxiv.org/pdf/2510.11566.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11566v1" 
            onclick="toggleFavorite(this, '2510.11566v1', 'SCOOP\'D: Learning Mixed-Liquid-Solid Scooping via Sim2Real Generative Policy')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kuanning Wang, Yongchong Gu, Yuqian Fu, Zeyu Shangguan, Sicheng He, Xiangyang Xue, Yanwei Fu, Daniel Seita

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-13

**备注**: Project page is at https://scoopdiff.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://scoopdiff.github.io/)

---

## 💡 一句话要点

**SCOOP'D：通过Sim2Real生成策略学习混合液体-固体抓取**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人抓取` `Sim2Real` `生成策略` `扩散模型` `混合液体-固体` `模仿学习` `OmniGibson`

## 📋 核心要点

1. 现有机器人抓取策略难以处理复杂的工具-物体交互，尤其是在涉及颗粒介质或液体等可变形物体时，面临无限维配置空间和复杂动力学挑战。
2. SCOOP'D利用仿真环境生成抓取演示数据，并使用扩散模型学习生成策略，从而模仿这些演示，实现从仿真到真实的迁移。
3. 实验表明，SCOOP'D在各种真实场景中表现出良好的零样本泛化能力，优于其他基线方法，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种名为SCOOP'D的方法，用于学习通用的机器人抓取策略，特别是针对混合液体-固体的场景。该方法利用OmniGibson（基于NVIDIA Omniverse构建）进行仿真，通过算法程序收集抓取演示数据，这些算法程序依赖于特权状态信息。然后，使用基于扩散模型的生成策略，从观测输入中模仿这些演示。该方法直接将学习到的策略应用于各种真实场景，测试其在不同物品数量、物品特性和容器类型下的性能。在零样本部署中，该方法在465次试验中表现出良好的效果，涵盖了不同难度的物品（分为“Level 1”和“Level 2”）。SCOOP'D优于所有基线和消融实验，表明这是一种有前景的机器人抓取技能获取方法。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人自主抓取混合液体-固体的问题，例如用勺子或勺子从容器中舀取物体。现有方法难以处理此类任务，因为它们需要对复杂的工具-物体交互进行推理，并且难以处理可变形物体（如颗粒介质或液体）的无限维配置空间和复杂动力学。

**核心思路**：论文的核心思路是利用仿真环境生成高质量的抓取演示数据，然后使用生成策略（具体为扩散模型）来模仿这些演示，从而学习到能够在真实世界中泛化的抓取策略。这种Sim2Real的方法可以避免在真实环境中收集大量数据的困难，并利用仿真环境的优势来探索各种抓取策略。

**技术框架**：SCOOP'D的整体框架包括以下几个主要阶段：1) 在OmniGibson仿真环境中，使用算法程序生成抓取演示数据。这些程序利用特权状态信息（例如物体的位置和速度）来确保生成高质量的演示。2) 使用扩散模型学习一个生成策略，该策略能够从观测输入（例如图像）中预测抓取动作。3) 将学习到的策略直接部署到真实机器人上，进行零样本测试。

**关键创新**：该论文的关键创新在于使用生成策略（扩散模型）来学习抓取策略，并将其应用于Sim2Real场景。与传统的模仿学习方法相比，生成策略能够更好地处理观测噪声和状态不确定性，从而提高策略的泛化能力。此外，该论文还提出了一种利用特权状态信息生成高质量仿真演示数据的方法。

**关键设计**：在仿真环境中，论文使用基于规则的算法来生成抓取演示数据。这些算法考虑了物体的位置、形状和数量等因素，并生成一系列抓取动作。扩散模型使用U-Net架构，并经过训练以从观测输入中预测抓取动作。损失函数包括动作预测损失和状态预测损失。论文还探索了不同的扩散模型参数设置，例如扩散步数和噪声水平。

## 📊 实验亮点

SCOOP'D在465次真实世界试验中表现出优异的零样本泛化能力，成功处理了不同难度级别（Level 1和Level 2）的物体。实验结果表明，SCOOP'D显著优于所有基线方法和消融实验，证明了其在机器人抓取任务中的有效性。项目网页提供了更多实验细节和视频。

## 🎯 应用场景

该研究具有广泛的应用前景，包括辅助喂食、灾难现场物品搜寻、自动化餐饮服务等。通过学习通用的抓取策略，机器人可以更好地适应各种复杂的环境和任务，提高工作效率和安全性。未来，该技术可以进一步扩展到其他类型的操作任务，例如装配、清洁等。

## 📄 摘要（原文）

> Scooping items with tools such as spoons and ladles is common in daily life, ranging from assistive feeding to retrieving items from environmental disaster sites. However, developing a general and autonomous robotic scooping policy is challenging since it requires reasoning about complex tool-object interactions. Furthermore, scooping often involves manipulating deformable objects, such as granular media or liquids, which is challenging due to their infinite-dimensional configuration spaces and complex dynamics. We propose a method, SCOOP'D, which uses simulation from OmniGibson (built on NVIDIA Omniverse) to collect scooping demonstrations using algorithmic procedures that rely on privileged state information. Then, we use generative policies via diffusion to imitate demonstrations from observational input. We directly apply the learned policy in diverse real-world scenarios, testing its performance on various item quantities, item characteristics, and container types. In zero-shot deployment, our method demonstrates promising results across 465 trials in diverse scenarios, including objects of different difficulty levels that we categorize as "Level 1" and "Level 2." SCOOP'D outperforms all baselines and ablations, suggesting that this is a promising approach to acquiring robotic scooping skills. Project page is at https://scoopdiff.github.io/.

