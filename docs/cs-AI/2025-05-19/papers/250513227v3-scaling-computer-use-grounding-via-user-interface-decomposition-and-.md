---
layout: default
title: Scaling Computer-Use Grounding via User Interface Decomposition and Synthesis
---

# Scaling Computer-Use Grounding via User Interface Decomposition and Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13227" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13227v3</a>
  <a href="https://arxiv.org/pdf/2505.13227.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13227v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13227v3', 'Scaling Computer-Use Grounding via User Interface Decomposition and Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianbao Xie, Jiaqi Deng, Xiaochuan Li, Junlin Yang, Haoyuan Wu, Jixuan Chen, Wenjing Hu, Xinyuan Wang, Yuhui Xu, Zekun Wang, Yiheng Xu, Junli Wang, Doyen Sahoo, Tao Yu, Caiming Xiong

**分类**: cs.AI, cs.CL, cs.CV, cs.HC

**发布日期**: 2025-05-19 (更新: 2025-10-24)

**备注**: 49 pages, 13 figures

---

## 💡 一句话要点

**提出OSWorld-G基准与Jedi数据集以解决GUI基础的自然语言指令映射问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图形用户界面` `自然语言处理` `计算机视觉` `数据集构建` `模型训练` `多尺度学习` `人机交互` `软件常识`

## 📋 核心要点

1. 现有方法在图形用户界面基础的自然语言指令映射中存在简化问题，无法处理复杂的真实世界交互。
2. 本文提出OSWorld-G基准和Jedi数据集，通过多视角任务解耦合，提供更全面的训练数据。
3. 实验结果显示，使用Jedi训练的模型在多个基准测试中表现优异，显著提升了代理能力。

## 📝 摘要（中文）

图形用户界面（GUI）基础的指令映射能力仍然是计算机使用代理开发中的一个关键瓶颈。现有基准过于简化任务，未能捕捉真实世界交互的复杂性。为此，本文提出OSWorld-G基准，包含564个精细注释的样本，涵盖文本匹配、元素识别、布局理解和精确操作等多种任务类型。同时，我们合成并发布了最大的计算机使用基础数据集Jedi，包含400万个示例。通过在Jedi上训练的多尺度模型，证明其在ScreenSpot-v2、ScreenSpot-Pro和OSWorld-G上的有效性。此外，改进的基础模型在复杂计算机任务上的代理能力也显著提升，从5%提高到27%。

## 🔬 方法详解

**问题定义**：本文旨在解决图形用户界面（GUI）基础的自然语言指令映射问题。现有方法通常将任务简化为短语表达，未能有效处理复杂的用户交互和软件常识。

**核心思路**：论文提出OSWorld-G基准和Jedi数据集，通过多视角解耦合任务，提供丰富的训练样本，以增强模型的理解和操作能力。

**技术框架**：整体架构包括数据收集、样本注释、模型训练和评估四个主要阶段。OSWorld-G基准用于评估模型在不同任务上的表现，而Jedi数据集则为模型提供了多样化的训练样本。

**关键创新**：最重要的技术创新在于构建了一个包含564个样本的OSWorld-G基准和400万个示例的Jedi数据集，显著提升了模型在复杂任务中的表现。与现有方法相比，这种方法更好地捕捉了用户界面的复杂性。

**关键设计**：在模型训练中，采用了多尺度模型架构，结合了不同界面元素的专用数据，以实现对新界面的组合泛化。损失函数和网络结构经过精心设计，以优化模型在具体任务上的表现。

## 📊 实验亮点

实验结果表明，使用Jedi数据集训练的多尺度模型在ScreenSpot-v2、ScreenSpot-Pro和OSWorld-G基准上均表现优异，性能提升幅度达到22%。在复杂计算机任务中，模型的代理能力从5%提升至27%，显示出显著的改进效果。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化办公软件和人机交互系统等。通过提升计算机使用代理的自然语言理解能力，可以显著改善用户体验，推动智能化办公和自动化技术的发展，未来可能在各类软件应用中得到广泛应用。

## 📄 摘要（原文）

> Graphical user interface (GUI) grounding, the ability to map natural language instructions to specific actions on graphical user interfaces, remains a critical bottleneck in computer use agent development. Current benchmarks oversimplify grounding tasks as short referring expressions, failing to capture the complexity of real-world interactions that require software commonsense, layout understanding, and fine-grained manipulation capabilities. To address these limitations, we introduce OSWorld-G, a comprehensive benchmark comprising 564 finely annotated samples across diverse task types including text matching, element recognition, layout understanding, and precise manipulation. Additionally, we synthesize and release the largest computer use grounding dataset Jedi, which contains 4 million examples through multi-perspective decoupling of tasks. Our multi-scale models trained on Jedi demonstrate its effectiveness by outperforming existing approaches on ScreenSpot-v2, ScreenSpot-Pro, and our OSWorld-G. Furthermore, we demonstrate that improved grounding with Jedi directly enhances agentic capabilities of general foundation models on complex computer tasks, improving from 5% to 27% on OSWorld. Through detailed ablation studies, we identify key factors contributing to grounding performance and verify that combining specialized data for different interface elements enables compositional generalization to novel interfaces. All benchmark, data, checkpoints, and code are open-sourced and available at https://osworld-grounding.github.io.

