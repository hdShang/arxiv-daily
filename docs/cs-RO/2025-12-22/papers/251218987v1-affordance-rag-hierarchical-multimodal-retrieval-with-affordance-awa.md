---
layout: default
title: "Affordance RAG: Hierarchical Multimodal Retrieval with Affordance-Aware Embodied Memory for Mobile Manipulation"
---

# Affordance RAG: Hierarchical Multimodal Retrieval with Affordance-Aware Embodied Memory for Mobile Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18987" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18987v1</a>
  <a href="https://arxiv.org/pdf/2512.18987.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18987v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18987v1', 'Affordance RAG: Hierarchical Multimodal Retrieval with Affordance-Aware Embodied Memory for Mobile Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryosuke Korekata, Quanting Xie, Yonatan Bisk, Komei Sugiura

**分类**: cs.RO, cs.CL, cs.CV

**发布日期**: 2025-12-22

**备注**: Accepted to IEEE RA-L, with presentation at ICRA 2026

---

## 💡 一句话要点

**Affordance RAG：用于移动操作的具身记忆分层多模态检索**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动操作` `具身智能` `可供性` `多模态检索` `自然语言理解`

## 📋 核心要点

1. 现有移动操作方法难以理解视觉语义和操作动作的可供性，导致任务成功率较低。
2. Affordance RAG通过构建可供性感知具身记忆，并结合分层多模态检索来解决上述问题。
3. 实验结果表明，该方法在检索性能和真实世界任务成功率方面均优于现有方法，任务成功率达到85%。

## 📝 摘要（中文）

本研究旨在解决开放词汇移动操作问题，即机器人需要根据自由形式的自然语言指令将各种物体运送到容器中。这项任务极具挑战性，因为它涉及理解视觉语义和操作动作的可供性。为了应对这些挑战，我们提出了一种零样本分层多模态检索框架Affordance RAG，该框架从预先探索的图像构建可供性感知具身记忆。该模型基于区域和视觉语义检索候选目标，并使用可供性得分对其进行重新排序，从而使机器人能够识别在真实环境中可能执行的操作选项。我们的方法在大型室内环境中移动操作指令的检索性能方面优于现有方法。此外，在机器人根据自由形式指令在室内环境中执行移动操作的真实世界实验中，所提出的方法实现了85%的任务成功率，在检索性能和整体任务成功率方面均优于现有方法。

## 🔬 方法详解

**问题定义**：论文旨在解决开放词汇移动操作任务，即机器人需要根据自然语言指令将物体移动到指定地点。现有方法的痛点在于难以理解视觉语义和操作动作的可供性，导致机器人无法准确识别目标和执行操作。例如，机器人可能无法区分相似的物体，或者无法判断某个物体是否适合放置在某个容器中。

**核心思路**：论文的核心思路是利用预先探索的图像构建可供性感知具身记忆，并结合分层多模态检索来提高机器人对目标和操作的理解能力。通过可供性感知，机器人可以更好地判断哪些操作是可行的，从而提高任务成功率。分层多模态检索则可以更有效地利用视觉和语义信息，从而更准确地识别目标。

**技术框架**：Affordance RAG框架包含以下几个主要模块：1) **具身记忆构建**：利用预先探索的图像构建可供性感知具身记忆。2) **分层多模态检索**：首先基于区域和视觉语义检索候选目标，然后使用可供性得分对候选目标进行重新排序。3) **操作执行**：根据检索结果执行相应的操作。整个流程是零样本的，不需要针对特定任务进行训练。

**关键创新**：该论文最重要的技术创新点在于提出了可供性感知具身记忆和分层多模态检索相结合的方法。可供性感知具身记忆可以帮助机器人更好地理解操作动作的可行性，而分层多模态检索可以更有效地利用视觉和语义信息。与现有方法相比，该方法能够更准确地识别目标和执行操作，从而提高任务成功率。

**关键设计**：在具身记忆构建阶段，论文使用了预训练的视觉模型来提取图像特征，并使用可供性预测模型来预测每个区域的可供性得分。在分层多模态检索阶段，论文首先使用CLIP模型来提取文本和图像特征，然后使用余弦相似度来计算文本和图像之间的相似度。最后，使用可供性得分对候选目标进行重新排序，选择得分最高的作为最终目标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18987v1/figs/eyecatch/RA-L25_eye-catch-v6.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18987v1/figs/framework/RA-L25_framework-v5.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18987v1/figs/simulated/simulated_sr_v2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在真实世界实验中取得了显著的成果，任务成功率达到85%，显著优于现有方法。在检索性能方面，该方法也优于现有方法，表明其能够更准确地识别目标。这些结果表明，该方法在解决开放词汇移动操作问题方面具有很大的潜力。

## 🎯 应用场景

该研究成果可应用于各种需要机器人进行移动操作的场景，例如家庭服务、仓储物流、医疗护理等。通过理解自然语言指令和环境信息，机器人可以更自主地完成任务，提高工作效率和服务质量。未来，该技术还可以扩展到更复杂的任务，例如多机器人协作、动态环境适应等。

## 📄 摘要（原文）

> In this study, we address the problem of open-vocabulary mobile manipulation, where a robot is required to carry a wide range of objects to receptacles based on free-form natural language instructions. This task is challenging, as it involves understanding visual semantics and the affordance of manipulation actions. To tackle these challenges, we propose Affordance RAG, a zero-shot hierarchical multimodal retrieval framework that constructs Affordance-Aware Embodied Memory from pre-explored images. The model retrieves candidate targets based on regional and visual semantics and reranks them with affordance scores, allowing the robot to identify manipulation options that are likely to be executable in real-world environments. Our method outperformed existing approaches in retrieval performance for mobile manipulation instruction in large-scale indoor environments. Furthermore, in real-world experiments where the robot performed mobile manipulation in indoor environments based on free-form instructions, the proposed method achieved a task success rate of 85%, outperforming existing methods in both retrieval performance and overall task success.

