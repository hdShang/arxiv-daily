---
layout: default
title: "OVSegDT: Segmenting Transformer for Open-Vocabulary Object Goal Navigation"
---

# OVSegDT: Segmenting Transformer for Open-Vocabulary Object Goal Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11479" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11479v1</a>
  <a href="https://arxiv.org/pdf/2508.11479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11479v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11479v1', 'OVSegDT: Segmenting Transformer for Open-Vocabulary Object Goal Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tatiana Zemskova, Aleksei Staroverov, Dmitry Yudin, Aleksandr Panov

**分类**: cs.RO

**发布日期**: 2025-08-15

**🔗 代码/项目**: [GITHUB](https://github.com/CognitiveAISystems/OVSegDT)

---

## 💡 一句话要点

**提出OVSegDT以解决开放词汇目标导航中的泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇导航` `变换器` `智能体` `语义分支` `熵自适应损失`

## 📋 核心要点

1. 现有的目标导航方法在小型数据集上过拟合，导致泛化能力不足和频繁碰撞等不安全行为。
2. OVSegDT通过引入语义分支和熵自适应损失调制，提供精确的空间线索并动态平衡信号，解决了现有方法的不足。
3. 实验结果显示，OVSegDT在未见类别上的表现与已见类别相当，且训练样本复杂度降低33%，碰撞次数减少50%。

## 📝 摘要（中文）

开放词汇目标导航要求具身智能体根据自由形式的语言描述到达目标物体，包括训练期间未见过的类别。现有的端到端策略在小型模拟器数据集上过拟合，虽然在训练场景中表现良好，但在泛化能力上不足，且常常表现出不安全行为（频繁碰撞）。我们提出了OVSegDT，这是一种轻量级的变换器策略，通过两个协同组件来解决这些问题。第一个组件是语义分支，包括目标二进制掩膜的编码器和辅助分割损失函数，能够为文本目标提供精确的空间线索。第二个组件是提出的熵自适应损失调制，这是一种每样本调度器，根据策略熵持续平衡模仿和强化信号，消除了脆弱的手动阶段切换。这些改进将训练的样本复杂度降低了33%，并将碰撞次数减少了一半，同时保持低推理成本（130M参数，仅RGB输入）。在HM3D-OVON上，我们的模型在未见类别上的表现与已见类别相当，并在没有深度、里程计或大型视觉语言模型的情况下，建立了最新的结果（验证集未见类别的成功率为40.1%，路径长度比为20.9%）。代码可在https://github.com/CognitiveAISystems/OVSegDT获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决开放词汇目标导航中智能体无法泛化到未见类别的问题。现有方法在小型模拟器数据集上训练，导致在真实场景中表现不佳，且存在安全隐患，如频繁碰撞。

**核心思路**：OVSegDT的核心思路是通过引入语义分支和熵自适应损失调制来增强智能体的导航能力。语义分支提供了目标的精确空间信息，而熵自适应损失调制则动态调整模仿和强化学习信号的平衡，从而提高训练效率和安全性。

**技术框架**：OVSegDT的整体架构包括两个主要模块：语义分支和熵自适应损失调制。语义分支负责处理目标的二进制掩膜，并通过辅助分割损失函数来增强目标的空间定位能力。熵自适应损失调制则根据策略的熵值动态调整训练信号的权重。

**关键创新**：OVSegDT的关键创新在于其熵自适应损失调制机制，这一机制能够消除传统方法中脆弱的手动阶段切换，提升了训练的稳定性和效率。

**关键设计**：在设计上，OVSegDT采用了130M参数的轻量级网络结构，输入仅为RGB图像。损失函数包括辅助分割损失，以增强语义分支的效果，同时熵自适应调制确保了训练过程中的信号平衡。整体设计旨在降低训练复杂度并提高智能体的安全性。

## 📊 实验亮点

OVSegDT在HM3D-OVON数据集上取得了显著的实验结果，未见类别的成功率达到40.1%，路径长度比为20.9%。相比于传统方法，其训练样本复杂度降低了33%，碰撞次数减少了一半，展示了其在实际应用中的优越性。

## 🎯 应用场景

OVSegDT在开放词汇目标导航领域具有广泛的应用潜力，尤其是在机器人导航、智能家居和自动驾驶等场景中。其能够处理未见类别的能力，使得智能体在复杂和动态环境中更加灵活和安全，未来可能推动更智能的自主系统的发展。

## 📄 摘要（原文）

> Open-vocabulary Object Goal Navigation requires an embodied agent to reach objects described by free-form language, including categories never seen during training. Existing end-to-end policies overfit small simulator datasets, achieving high success on training scenes but failing to generalize and exhibiting unsafe behaviour (frequent collisions). We introduce OVSegDT, a lightweight transformer policy that tackles these issues with two synergistic components. The first component is the semantic branch, which includes an encoder for the target binary mask and an auxiliary segmentation loss function, grounding the textual goal and providing precise spatial cues. The second component consists of a proposed Entropy-Adaptive Loss Modulation, a per-sample scheduler that continuously balances imitation and reinforcement signals according to the policy entropy, eliminating brittle manual phase switches. These additions cut the sample complexity of training by 33%, and reduce collision count in two times while keeping inference cost low (130M parameters, RGB-only input). On HM3D-OVON, our model matches the performance on unseen categories to that on seen ones and establishes state-of-the-art results (40.1% SR, 20.9% SPL on val unseen) without depth, odometry, or large vision-language models. Code is available at https://github.com/CognitiveAISystems/OVSegDT.

