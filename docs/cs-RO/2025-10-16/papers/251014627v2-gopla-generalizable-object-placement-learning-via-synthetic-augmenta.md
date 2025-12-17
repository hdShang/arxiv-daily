---
layout: default
title: GOPLA: Generalizable Object Placement Learning via Synthetic Augmentation of Human Arrangement
---

# GOPLA: Generalizable Object Placement Learning via Synthetic Augmentation of Human Arrangement

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14627" target="_blank" class="toolbar-btn">arXiv: 2510.14627v2</a>
    <a href="https://arxiv.org/pdf/2510.14627.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14627v2" 
            onclick="toggleFavorite(this, '2510.14627v2', 'GOPLA: Generalizable Object Placement Learning via Synthetic Augmentation of Human Arrangement')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yao Zhong, Hanzhi Chen, Simon Schaefer, Anran Zhang, Stefan Leutenegger

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-16 (更新: 2025-10-25)

---

## 💡 一句话要点

**GOPLA：通过合成增强人类布置数据，学习可泛化的物体放置**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物体放置` `机器人` `多模态学习` `扩散模型` `合成数据增强` `大语言模型` `可供性图`

## 📋 核心要点

1. 机器人辅助日常家居整理面临物体放置难题，需要推理语义偏好和几何可行性。
2. GOPLA利用多模态大语言模型和扩散模型，从增强的人类演示中学习物体放置策略。
3. 实验表明，GOPLA在真实机器人场景中，物体放置成功率显著提升，泛化能力强。

## 📝 摘要（中文）

本文提出GOPLA，一个分层框架，通过增强的人类演示学习可泛化的物体放置。该框架利用多模态大型语言模型将人类指令和视觉输入转化为结构化的规划，这些规划指定了成对的物体关系。然后，空间映射器将这些规划转化为具有几何常识的3D可供性图。基于扩散的规划器生成放置姿态，并考虑测试时的代价、多规划分布和避碰。为了克服数据稀缺问题，本文引入了一个可扩展的流程，将人类放置演示扩展为多样化的合成训练数据。大量实验表明，在定位精度和物理合理性方面，GOPLA的放置成功率比第二名提高了30.04个百分点，展示了在各种真实机器人放置场景中的强大泛化能力。

## 🔬 方法详解

**问题定义**：物体放置任务需要机器人理解人类指令，并根据语义关系和几何约束，将物体放置在合适的位置。现有方法在数据稀缺的情况下，泛化能力不足，难以应对真实场景中的复杂情况。

**核心思路**：GOPLA的核心思路是利用多模态大语言模型理解人类指令，生成结构化的物体关系规划，并结合扩散模型生成符合几何约束的放置姿态。通过合成数据增强，提高模型的泛化能力。

**技术框架**：GOPLA框架包含三个主要模块：1) 多模态大语言模型：将人类指令和视觉输入转化为结构化的规划，描述物体之间的关系。2) 空间映射器：将规划转化为3D可供性图，赋予几何常识。3) 基于扩散的规划器：生成放置姿态，考虑测试时的代价、多规划分布和避碰。

**关键创新**：GOPLA的关键创新在于：1) 提出了一种分层框架，将语义理解和几何推理相结合。2) 利用多模态大语言模型进行语义理解，生成结构化的规划。3) 引入了基于扩散的规划器，生成符合几何约束的放置姿态。4) 提出了一个可扩展的合成数据生成流程，克服了数据稀缺问题。

**关键设计**：多模态大语言模型采用预训练的语言模型，并结合视觉编码器进行微调。空间映射器使用卷积神经网络学习3D可供性图。基于扩散的规划器使用U-Net结构，以测试时的代价作为条件，生成放置姿态。合成数据生成流程通过随机改变物体的位置、姿态和环境，生成多样化的训练数据。

## 📊 实验亮点

实验结果表明，GOPLA在真实机器人放置场景中表现出色，放置成功率比第二名提高了30.04个百分点。这证明了GOPLA在定位精度和物理合理性方面的优势，以及在各种真实场景中的强大泛化能力。

## 🎯 应用场景

GOPLA可应用于家庭服务机器人、仓库自动化、智能制造等领域。它可以帮助机器人理解人类指令，完成物体放置任务，提高工作效率和智能化水平。未来，GOPLA可以扩展到更复杂的场景，例如家具组装、环境布置等。

## 📄 摘要（原文）

> Robots are expected to serve as intelligent assistants, helping humans with everyday household organization. A central challenge in this setting is the task of object placement, which requires reasoning about both semantic preferences (e.g., common-sense object relations) and geometric feasibility (e.g., collision avoidance). We present GOPLA, a hierarchical framework that learns generalizable object placement from augmented human demonstrations. A multi-modal large language model translates human instructions and visual inputs into structured plans that specify pairwise object relationships. These plans are then converted into 3D affordance maps with geometric common sense by a spatial mapper, while a diffusion-based planner generates placement poses guided by test-time costs, considering multi-plan distributions and collision avoidance. To overcome data scarcity, we introduce a scalable pipeline that expands human placement demonstrations into diverse synthetic training data. Extensive experiments show that our approach improves placement success rates by 30.04 percentage points over the runner-up, evaluated on positioning accuracy and physical plausibility, demonstrating strong generalization across a wide range of real-world robotic placement scenarios.

