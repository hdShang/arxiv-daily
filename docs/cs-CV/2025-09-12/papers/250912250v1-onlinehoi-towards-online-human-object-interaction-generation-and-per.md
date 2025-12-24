---
layout: default
title: "OnlineHOI: Towards Online Human-Object Interaction Generation and Perception"
---

# OnlineHOI: Towards Online Human-Object Interaction Generation and Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12250" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12250v1</a>
  <a href="https://arxiv.org/pdf/2509.12250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12250v1', 'OnlineHOI: Towards Online Human-Object Interaction Generation and Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihong Ji, Yunze Liu, Yiyao Zhuo, Weijiang Yu, Fei Ma, Joshua Huang, Fei Yu

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-09-12

**备注**: Accepted at ACM MM 2025

---

## 💡 一句话要点

**提出OnlineHOI框架，用于在线人-物交互生成与感知任务**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人-物交互` `在线学习` `Mamba架构` `记忆机制` `序列建模` `行为预测` `机器人`

## 📋 核心要点

1. 现有HOI方法主要在离线环境下进行，无法有效处理现实场景中在线HOI生成与感知任务。
2. 提出OnlineHOI框架，利用Mamba架构处理流数据，并结合记忆机制有效整合历史信息。
3. 在Core4D、OAKINK2和HOI4D数据集上，OnlineHOI框架在在线HOI生成和感知任务中取得了SOTA结果。

## 📝 摘要（中文）

人-物交互(HOI)的感知和生成对于机器人、AR/VR和人类行为理解等领域至关重要。然而，当前的方法通常在离线环境中建模，即每个时间步的信息可以从整个交互序列中获取。与此相反，在现实场景中，每个时间步可用的信息仅来自当前时刻和历史数据，即在线环境。我们发现离线方法在在线环境中表现不佳。基于此，我们提出了两个新任务：在线HOI生成和感知。为了解决这些任务，我们引入了OnlineHOI框架，这是一个基于Mamba框架并采用记忆机制的网络架构。通过利用Mamba强大的流数据建模能力和记忆机制对历史信息的有效整合，我们在Core4D和OAKINK2在线生成任务以及在线HOI4D感知任务上取得了最先进的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决在线人-物交互（HOI）的生成和感知问题。现有方法主要在离线环境下进行建模，即可以访问整个交互序列的信息。然而，在实际应用中，系统只能获取当前时刻和历史数据，这导致离线方法在在线场景下性能显著下降。因此，论文提出了在线HOI生成和感知这两个新任务，以更贴近实际应用。

**核心思路**：论文的核心思路是利用Mamba架构处理流数据，并结合记忆机制有效整合历史信息。Mamba架构擅长处理序列数据，能够捕捉时间依赖关系。记忆机制则允许模型存储和检索历史信息，从而更好地理解和预测未来的交互。

**技术框架**：OnlineHOI框架主要由Mamba模块和记忆模块组成。Mamba模块负责处理当前的输入数据，提取特征并预测HOI。记忆模块则负责存储历史信息，并根据当前输入动态地更新记忆。在每个时间步，Mamba模块首先处理当前输入，然后记忆模块根据当前输入更新记忆，最后Mamba模块结合当前输入和记忆信息进行HOI预测。

**关键创新**：该论文的关键创新在于将Mamba架构和记忆机制结合起来，用于解决在线HOI生成和感知问题。Mamba架构能够有效地处理流数据，而记忆机制则能够有效地整合历史信息。这种结合使得OnlineHOI框架能够更好地理解和预测未来的交互。

**关键设计**：论文中，记忆模块的设计至关重要。具体来说，记忆模块采用了一种基于注意力的机制，允许模型根据当前输入动态地选择需要关注的历史信息。此外，论文还设计了一种损失函数，用于鼓励模型学习到有效的记忆表示。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

OnlineHOI框架在Core4D和OAKINK2在线生成任务以及在线HOI4D感知任务上取得了SOTA结果。实验结果表明，OnlineHOI框架能够有效地利用历史信息，从而显著提高在线HOI生成和感知的性能。与现有方法相比，OnlineHOI框架在各项指标上均有显著提升，证明了其有效性和优越性。

## 🎯 应用场景

该研究成果可广泛应用于机器人、AR/VR、智能监控、人机交互等领域。例如，在机器人领域，机器人可以利用该技术实时感知和预测人类的动作，从而更好地与人类进行协作。在AR/VR领域，该技术可以用于创建更逼真和自然的虚拟交互体验。在智能监控领域，该技术可以用于检测和识别异常行为。

## 📄 摘要（原文）

> The perception and generation of Human-Object Interaction (HOI) are crucial for fields such as robotics, AR/VR, and human behavior understanding. However, current approaches model this task in an offline setting, where information at each time step can be drawn from the entire interaction sequence. In contrast, in real-world scenarios, the information available at each time step comes only from the current moment and historical data, i.e., an online setting. We find that offline methods perform poorly in an online context. Based on this observation, we propose two new tasks: Online HOI Generation and Perception. To address this task, we introduce the OnlineHOI framework, a network architecture based on the Mamba framework that employs a memory mechanism. By leveraging Mamba's powerful modeling capabilities for streaming data and the Memory mechanism's efficient integration of historical information, we achieve state-of-the-art results on the Core4D and OAKINK2 online generation tasks, as well as the online HOI4D perception task.

