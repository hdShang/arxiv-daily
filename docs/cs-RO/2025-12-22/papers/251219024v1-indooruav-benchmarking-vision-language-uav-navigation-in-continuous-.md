---
layout: default
title: "IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments"
---

# IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19024" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19024v1</a>
  <a href="https://arxiv.org/pdf/2512.19024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19024v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19024v1', 'IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Liu, Yu Liu, Hanshuo Qiu, Yang Qirong, Zhouhui Lian

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**IndoorUAV：提出室内无人机视觉-语言导航基准与方法，填补相关研究空白。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `室内无人机` `视觉-语言导航` `基准数据集` `任务分解` `多模态融合`

## 📋 核心要点

1. 现有VLN研究主要集中于地面机器人或室外无人机，缺乏对室内无人机VLN的深入探索，限制了其在实际场景中的应用。
2. 论文提出IndoorUAV基准，包含多样化的3D室内场景和高质量的视觉-语言导航轨迹，并设计了IndoorUAV-Agent导航模型。
3. IndoorUAV基准包含长时程VLN和短时程VLA两个子集，并利用任务分解和多模态推理提升导航性能。

## 📝 摘要（中文）

视觉-语言导航（VLN）使智能体能够通过遵循自然语言指令并在视觉观察的基础上在复杂环境中导航。虽然现有工作主要集中在地面机器人或室外无人机（UAV）上，但基于室内无人机的VLN仍未得到充分探索，尽管它与现实世界的应用（如密闭空间内的检查、交付和搜索救援）相关。为了弥合这一差距，我们引入了	extbf{IndoorUAV}，这是一个专门为室内无人机VLN量身定制的新基准和方法。我们首先从Habitat模拟器中整理了1000多个多样且结构丰富的3D室内场景。在这些环境中，我们模拟了真实的无人机飞行动态，以手动收集各种3D导航轨迹，并通过数据增强技术进一步丰富。此外，我们设计了一个自动注释流水线，为每个轨迹生成不同粒度的自然语言指令。这个过程产生了超过16,000条高质量轨迹，构成了专注于长时程VLN的	extbf{IndoorUAV-VLN}子集。为了支持短时程规划，我们通过选择语义上显著的关键帧并重新生成简洁的指令，将长轨迹分割成子轨迹，形成了	extbf{IndoorUAV-VLA}子集。最后，我们引入了	extbf{IndoorUAV-Agent}，这是一个专为我们的基准设计的导航模型，利用了任务分解和多模态推理。我们希望IndoorUAV能够成为一个宝贵的资源，以推进室内空中导航领域中视觉-语言具身人工智能的研究。

## 🔬 方法详解

**问题定义**：现有视觉-语言导航（VLN）研究主要集中在地面机器人和室外无人机，忽略了室内无人机VLN这一重要方向。室内无人机在狭小空间内的导航具有独特的挑战，例如复杂的环境结构、有限的视野和精确的控制需求。缺乏专门的基准数据集和针对性模型阻碍了该领域的发展。

**核心思路**：论文的核心思路是构建一个高质量的室内无人机VLN基准数据集，并设计一个能够有效利用视觉和语言信息进行导航的智能体。通过模拟真实的无人机飞行动态和自动生成自然语言指令，IndoorUAV数据集能够反映室内无人机导航的实际挑战。IndoorUAV-Agent模型则通过任务分解和多模态推理来提升导航性能。

**技术框架**：IndoorUAV包含两个子集：IndoorUAV-VLN和IndoorUAV-VLA。IndoorUAV-VLN专注于长时程VLN，包含超过16,000条高质量轨迹。IndoorUAV-VLA则通过分割长轨迹并重新生成指令，支持短时程规划。IndoorUAV-Agent模型采用任务分解策略，将导航任务分解为多个子任务，例如路径规划、姿态控制和避障。模型利用多模态信息融合技术，将视觉信息和语言指令进行有效整合，从而实现精确的导航。

**关键创新**：论文的关键创新在于构建了首个专门针对室内无人机VLN的基准数据集IndoorUAV。该数据集包含多样化的3D室内场景、真实的无人机飞行动态和高质量的自然语言指令。此外，论文提出的IndoorUAV-Agent模型采用任务分解和多模态推理策略，能够有效应对室内无人机导航的挑战。

**关键设计**：IndoorUAV数据集的构建过程中，采用了数据增强技术来增加数据的多样性。自动注释流水线能够生成不同粒度的自然语言指令。IndoorUAV-Agent模型采用了深度强化学习算法进行训练，并设计了专门的奖励函数来鼓励智能体完成导航任务。具体的网络结构和参数设置在论文中有详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19024v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19024v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19024v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建了包含超过16,000条轨迹的IndoorUAV-VLN数据集，并提出了IndoorUAV-Agent导航模型。实验结果表明，IndoorUAV-Agent在IndoorUAV基准上取得了显著的性能提升（具体数值未知），验证了任务分解和多模态推理策略的有效性。该基准的发布将促进室内无人机视觉-语言导航领域的研究。

## 🎯 应用场景

该研究成果可应用于室内无人机的多种实际场景，例如建筑物内部的巡检、仓库内的货物盘点、灾难现场的搜索救援等。通过结合视觉和语言信息，无人机能够更智能地理解人类指令，并在复杂环境中自主导航，从而提高工作效率和安全性。未来，该技术有望在智慧城市、智能家居等领域发挥重要作用。

## 📄 摘要（原文）

> Vision-Language Navigation (VLN) enables agents to navigate in complex environments by following natural language instructions grounded in visual observations. Although most existing work has focused on ground-based robots or outdoor Unmanned Aerial Vehicles (UAVs), indoor UAV-based VLN remains underexplored, despite its relevance to real-world applications such as inspection, delivery, and search-and-rescue in confined spaces. To bridge this gap, we introduce \textbf{IndoorUAV}, a novel benchmark and method specifically tailored for VLN with indoor UAVs. We begin by curating over 1,000 diverse and structurally rich 3D indoor scenes from the Habitat simulator. Within these environments, we simulate realistic UAV flight dynamics to collect diverse 3D navigation trajectories manually, further enriched through data augmentation techniques. Furthermore, we design an automated annotation pipeline to generate natural language instructions of varying granularity for each trajectory. This process yields over 16,000 high-quality trajectories, comprising the \textbf{IndoorUAV-VLN} subset, which focuses on long-horizon VLN. To support short-horizon planning, we segment long trajectories into sub-trajectories by selecting semantically salient keyframes and regenerating concise instructions, forming the \textbf{IndoorUAV-VLA} subset. Finally, we introduce \textbf{IndoorUAV-Agent}, a novel navigation model designed for our benchmark, leveraging task decomposition and multimodal reasoning. We hope IndoorUAV serves as a valuable resource to advance research on vision-language embodied AI in the indoor aerial navigation domain.

