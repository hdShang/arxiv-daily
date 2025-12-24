---
layout: default
title: "AssemMate: Graph-Based LLM for Robotic Assembly Assistance"
---

# AssemMate: Graph-Based LLM for Robotic Assembly Assistance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11617" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11617v1</a>
  <a href="https://arxiv.org/pdf/2509.11617.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11617v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11617v1', 'AssemMate: Graph-Based LLM for Robotic Assembly Assistance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Zheng, Chaoran Zhang, Zijian Liang, EnTe Lin, Shubo Cui, Qinghongbing Xie, Zhaobo Xu, Long Zeng

**分类**: cs.RO

**发布日期**: 2025-09-15

**🔗 代码/项目**: [GITHUB](https://github.com/cristina304/AssemMate.git)

---

## 💡 一句话要点

**提出AssemMate，利用图结构LLM辅助机器人进行装配任务。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人装配` `大型语言模型` `知识图谱` `图卷积网络` `人机交互` `视觉感知` `自监督学习`

## 📋 核心要点

1. 现有基于LLM的机器人装配辅助方法依赖自然语言文本表示知识，存在上下文过长和冗余的问题，难以满足机器人实时精确推理的需求。
2. AssemMate利用图结构作为知识表示，通过图卷积网络将知识图谱信息编码并与LLM对齐，实现高效的知识推理和人机交互。
3. 实验结果表明，AssemMate在准确率、推理速度和上下文长度方面均优于现有方法，并在模拟和真实环境中验证了其机器人抓取能力。

## 📝 摘要（中文）

基于大型语言模型（LLM）的机器人装配辅助已获得显著的研究关注。它需要注入领域特定知识，通过与人类的自然语言交互来指导装配过程。然而，现有方法以自然语言文本形式表示知识，由于上下文过长和内容冗余，难以满足机器人对实时和精确推理的需求。为了弥合这一差距，我们提出了AssemMate，它利用图——一种简洁而准确的知识表示形式——作为输入。这种基于图的LLM支持知识图谱问答（KGQA），从而支持人机交互和特定产品的装配任务规划。除了交互式问答，AssemMate还支持感知堆叠场景并执行抓取以辅助装配。具体来说，一种自监督图卷积网络（GCN）将知识图谱实体和关系编码到潜在空间中，并将其与LLM的表示对齐，使LLM能够理解图信息。此外，采用了一种视觉增强策略来解决抓取中的堆叠场景。通过训练和评估，AssemMate优于现有方法，实现了6.4%的更高准确率，3倍的更快推理速度和28倍的更短上下文长度，同时在随机图上表现出强大的泛化能力。我们的方法还通过模拟和真实环境中的机器人抓取实验进一步证明了优越性。

## 🔬 方法详解

**问题定义**：现有基于LLM的机器人装配辅助系统，主要依赖于自然语言文本来表示装配知识。这种方式存在两个主要问题：一是自然语言文本冗长，导致LLM推理效率低下；二是自然语言文本的模糊性可能导致机器人执行错误的操作。因此，需要一种更简洁、更精确的知识表示方法，以提高LLM的推理效率和准确性。

**核心思路**：AssemMate的核心思路是将装配知识表示为知识图谱，利用图结构来表达零件之间的关系和装配步骤。通过图卷积网络（GCN）将知识图谱的实体和关系编码成向量表示，并与LLM的嵌入空间对齐，使LLM能够理解和利用图结构信息进行推理和规划。这种方法可以有效减少上下文长度，提高推理速度，并提高装配任务的准确性。

**技术框架**：AssemMate的整体框架包括以下几个主要模块：1) 知识图谱构建模块：将装配知识表示为知识图谱，包括零件、装配步骤和它们之间的关系。2) 图卷积网络（GCN）编码模块：使用自监督GCN将知识图谱的实体和关系编码成向量表示。3) LLM对齐模块：将GCN编码的向量表示与LLM的嵌入空间对齐，使LLM能够理解图结构信息。4) 人机交互模块：通过自然语言与人类交互，接收指令并进行装配任务规划。5) 视觉感知模块：利用视觉信息感知堆叠场景，辅助机器人进行抓取。6) 机器人控制模块：控制机器人执行装配任务。

**关键创新**：AssemMate的关键创新在于使用图结构作为LLM的输入，将知识图谱与LLM相结合，从而实现高效的知识推理和装配任务规划。与现有方法相比，AssemMate能够显著减少上下文长度，提高推理速度，并提高装配任务的准确性。此外，AssemMate还采用了视觉增强策略来解决堆叠场景中的抓取问题。

**关键设计**：GCN采用自监督学习的方式进行训练，损失函数包括节点分类损失和链接预测损失，以提高GCN的编码能力。LLM对齐模块使用对比学习的方式，将GCN编码的向量表示与LLM的嵌入空间对齐。视觉增强策略使用深度学习模型来分割和识别堆叠的零件，并估计其位姿，从而辅助机器人进行抓取。

## 📊 实验亮点

AssemMate在实验中表现出显著的优势。与现有方法相比，AssemMate在装配任务中实现了6.4%的更高准确率，推理速度提高了3倍，上下文长度缩短了28倍。此外，AssemMate在随机图上表现出强大的泛化能力，并在模拟和真实环境中的机器人抓取实验中验证了其有效性。

## 🎯 应用场景

AssemMate可应用于各种需要人机协作的装配场景，例如电子产品组装、汽车零部件装配、航空航天设备装配等。该研究能够提高装配效率、降低错误率，并降低对人工操作员的技能要求。未来，AssemMate有望扩展到更复杂的装配任务，并与其他机器人技术相结合，实现更智能化的自动化装配。

## 📄 摘要（原文）

> Large Language Model (LLM)-based robotic assembly assistance has gained significant research attention. It requires the injection of domain-specific knowledge to guide the assembly process through natural language interaction with humans. Despite some progress, existing methods represent knowledge in the form of natural language text. Due to the long context and redundant content, they struggle to meet the robots' requirements for real-time and precise reasoning. In order to bridge this gap, we present AssemMate, which utilizes the graph\textemdash a concise and accurate form of knowledge representation\textemdash as input. This graph-based LLM enables knowledge graph question answering (KGQA), supporting human-robot interaction and assembly task planning for specific products. Beyond interactive QA, AssemMate also supports sensing stacked scenes and executing grasping to assist with assembly. Specifically, a self-supervised Graph Convolutional Network (GCN) encodes knowledge graph entities and relations into a latent space and aligns them with LLM's representation, enabling the LLM to understand graph information. In addition, a vision-enhanced strategy is employed to address stacked scenes in grasping. Through training and evaluation, AssemMate outperforms existing methods, achieving 6.4\% higher accuracy, 3 times faster inference, and 28 times shorter context length, while demonstrating strong generalization ability on random graphs. And our approach further demonstrates superiority through robotic grasping experiments in both simulated and real-world settings. More details can be found on the project page: https://github.com/cristina304/AssemMate.git

