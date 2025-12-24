---
layout: default
title: "KeySG: Hierarchical Keyframe-Based 3D Scene Graphs"
---

# KeySG: Hierarchical Keyframe-Based 3D Scene Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01049" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01049v1</a>
  <a href="https://arxiv.org/pdf/2510.01049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01049v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01049v1', 'KeySG: Hierarchical Keyframe-Based 3D Scene Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdelrhman Werby, Dennis Rotondi, Fabio Scaparro, Kai O. Arras

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**KeySG：基于分层关键帧的3D场景图构建，提升语义丰富性和可扩展性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景图` `关键帧` `视觉语言模型` `分层图` `检索增强生成`

## 📋 核心要点

1. 现有3D场景图构建方法在语义上受限于预定义的关系集合，且在大规模环境中的序列化容易超出LLM的上下文窗口。
2. KeySG通过分层图结构和关键帧多模态信息增强，结合VLM提取场景信息，避免显式关系建模，实现更通用的推理和规划。
3. 实验结果表明，KeySG在3D对象分割和复杂查询检索等任务上优于现有方法，验证了其语义丰富性和效率。

## 📝 摘要（中文）

本文提出了一种名为KeySG的框架，用于构建3D场景的分层图表示。该图由楼层、房间、物体和功能元素组成，节点通过关键帧提取的多模态信息进行增强，关键帧的选择旨在优化几何和视觉覆盖率。KeySG利用视觉语言模型（VLM）高效提取场景信息，避免了显式建模对象之间的关系，从而实现更通用、与任务无关的推理和规划。通过分层检索增强生成（RAG）流程，KeySG能够从图中提取相关上下文，从而处理复杂和模糊的查询，并缓解大型场景图的可扩展性问题。在包括3D对象分割和复杂查询检索在内的四个基准测试中，KeySG在大多数指标上优于现有方法，证明了其卓越的语义丰富性和效率。

## 🔬 方法详解

**问题定义**：现有3D场景图方法存在语义关系表达受限和可扩展性差的问题。具体来说，它们依赖于预定义的语义关系，难以捕捉复杂场景中的细粒度关系，并且在大规模场景中，场景图的序列化表示容易超出大型语言模型（LLM）的上下文窗口，限制了其应用。

**核心思路**：KeySG的核心思路是利用分层图结构和关键帧多模态信息来增强场景图的语义表达能力和可扩展性。通过关键帧选择优化几何和视觉覆盖率，并利用视觉语言模型（VLM）从关键帧中提取丰富的场景信息，从而避免了显式建模对象之间的复杂关系，简化了场景图的结构。

**技术框架**：KeySG框架包含以下主要模块：1) 关键帧选择模块，用于选择能够代表场景几何和视觉信息的关键帧；2) 多模态信息提取模块，利用VLM从关键帧中提取场景的语义信息，包括对象类别、属性和关系；3) 分层图构建模块，将场景表示为分层图，包括楼层、房间、对象和功能元素；4) 检索增强生成（RAG）模块，用于从分层图中检索相关上下文，并生成对复杂查询的响应。

**关键创新**：KeySG的关键创新在于：1) 提出了基于关键帧的多模态信息增强方法，利用VLM提取场景信息，避免了显式建模对象之间的关系，提高了语义表达能力；2) 采用了分层图结构，将场景分解为多个层次，提高了可扩展性，并支持高效的上下文检索；3) 结合了检索增强生成（RAG）流程，能够从图中提取相关上下文，处理复杂和模糊的查询。

**关键设计**：关键帧选择策略旨在最大化几何和视觉覆盖率，具体实现未知。VLM的选择和微调策略未知。分层图的构建规则和层次划分标准未知。RAG模块的检索策略和生成模型选择未知。损失函数和训练细节未知。

## 📊 实验亮点

KeySG在四个基准测试中进行了评估，包括3D对象分割和复杂查询检索。实验结果表明，KeySG在大多数指标上优于现有方法，证明了其卓越的语义丰富性和效率。具体性能数据和提升幅度在论文中给出，此处未知。

## 🎯 应用场景

KeySG在机器人导航、场景理解、人机交互等领域具有广泛的应用前景。它可以帮助机器人在复杂环境中进行推理、规划和导航，例如在家庭服务机器人、自动驾驶汽车和智能家居等应用中。此外，KeySG还可以用于增强现实和虚拟现实应用，提供更逼真的场景体验。

## 📄 摘要（原文）

> In recent years, 3D scene graphs have emerged as a powerful world representation, offering both geometric accuracy and semantic richness. Combining 3D scene graphs with large language models enables robots to reason, plan, and navigate in complex human-centered environments. However, current approaches for constructing 3D scene graphs are semantically limited to a predefined set of relationships, and their serialization in large environments can easily exceed an LLM's context window. We introduce KeySG, a framework that represents 3D scenes as a hierarchical graph consisting of floors, rooms, objects, and functional elements, where nodes are augmented with multi-modal information extracted from keyframes selected to optimize geometric and visual coverage. The keyframes allow us to efficiently leverage VLM to extract scene information, alleviating the need to explicitly model relationship edges between objects, enabling more general, task-agnostic reasoning and planning. Our approach can process complex and ambiguous queries while mitigating the scalability issues associated with large scene graphs by utilizing a hierarchical retrieval-augmented generation (RAG) pipeline to extract relevant context from the graph. Evaluated across four distinct benchmarks -- including 3D object segmentation and complex query retrieval -- KeySG outperforms prior approaches on most metrics, demonstrating its superior semantic richness and efficiency.

