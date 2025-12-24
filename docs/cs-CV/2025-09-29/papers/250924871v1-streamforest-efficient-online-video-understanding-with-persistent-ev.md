---
layout: default
title: "StreamForest: Efficient Online Video Understanding with Persistent Event Memory"
---

# StreamForest: Efficient Online Video Understanding with Persistent Event Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24871" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24871v1</a>
  <a href="https://arxiv.org/pdf/2509.24871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24871v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24871v1', 'StreamForest: Efficient Online Video Understanding with Persistent Event Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangyu Zeng, Kefan Qiu, Qingyu Zhang, Xinhao Li, Jing Wang, Jiaxin Li, Ziang Yan, Kun Tian, Meng Tian, Xinhai Zhao, Yi Wang, Limin Wang

**分类**: cs.CV

**发布日期**: 2025-09-29

**备注**: Accepted as a Spotlight at NeurIPS 2025

---

## 💡 一句话要点

**提出StreamForest，利用持久事件记忆实现高效的在线视频理解**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `流式视频理解` `持久事件记忆` `多模态大语言模型` `实时感知` `自动驾驶`

## 📋 核心要点

1. 现有MLLM在流式视频理解中，受限于历史视觉特征的存储约束和实时时空推理能力不足。
2. StreamForest通过持久事件记忆森林自适应组织视频帧，并利用细粒度时空窗口增强实时感知。
3. 在StreamingBench等基准测试中，StreamForest达到SOTA性能，并在token压缩下保持高准确率。

## 📝 摘要（中文）

本文提出了一种名为StreamForest的新型架构，专门为流式视频理解而设计。StreamForest的核心是持久事件记忆森林，这是一种能够自适应地将视频帧组织成多个事件级树结构的记忆机制。该过程由基于时间距离、内容相似性和合并频率的惩罚函数引导，从而在有限的计算资源下实现高效的长期记忆保持。为了增强实时感知，引入了细粒度时空窗口，捕捉详细的短期视觉线索，以改善当前场景的感知。此外，还提出了OnlineIT，这是一个专为流式视频任务定制的指令调优数据集，显著提升了MLLM在实时感知和未来预测方面的性能。为了评估在实际应用中的泛化能力，引入了ODV-Bench，这是一个专注于自动驾驶场景中实时流式视频理解的新基准。实验结果表明，StreamForest实现了最先进的性能，在StreamingBench、OVBench和OVO-Bench上的准确率分别为77.3%、60.5%和55.6%。特别是在极端的视觉token压缩下（限制为1024个token），该模型相对于默认设置，在八个基准测试中仍保持了96.8%的平均准确率。这些结果突显了StreamForest在流式视频理解方面的鲁棒性、效率和泛化能力。

## 🔬 方法详解

**问题定义**：现有方法在处理流式视频理解任务时，面临着如何有效存储和利用历史信息，以及如何进行实时时空推理的挑战。传统方法要么存储所有历史帧，导致存储压力巨大；要么简单地丢弃历史信息，导致长期依赖关系丢失。因此，如何在有限的计算资源下，实现高效的长期记忆保持和实时感知是亟待解决的问题。

**核心思路**：StreamForest的核心思路是构建一个持久事件记忆森林，将视频帧自适应地组织成多个事件级别的树结构。通过这种方式，模型可以有效地压缩和存储历史信息，同时保留关键的事件信息。此外，通过引入细粒度时空窗口，模型可以捕捉到详细的短期视觉线索，从而增强实时感知能力。

**技术框架**：StreamForest的整体架构包含以下几个主要模块：1) 特征提取模块：用于提取视频帧的视觉特征。2) 持久事件记忆森林：用于存储和组织历史视觉特征，构建事件级别的树结构。3) 细粒度时空窗口：用于捕捉短期视觉线索，增强实时感知。4) MLLM：用于进行视频理解任务，例如视频问答、行为识别等。整个流程是，首先提取视频帧的特征，然后将其存储到持久事件记忆森林中，同时利用细粒度时空窗口捕捉短期视觉线索，最后将这些信息输入到MLLM中进行推理。

**关键创新**：StreamForest最重要的技术创新点在于持久事件记忆森林的设计。与传统的记忆机制不同，持久事件记忆森林可以自适应地组织视频帧，并根据时间距离、内容相似性和合并频率等因素进行更新。这种自适应的组织方式可以有效地压缩和存储历史信息，同时保留关键的事件信息。此外，细粒度时空窗口的设计也增强了模型对短期视觉线索的感知能力。

**关键设计**：持久事件记忆森林的关键设计包括：1) 惩罚函数：用于指导视频帧的组织和更新，基于时间距离、内容相似性和合并频率等因素。2) 树结构：用于存储和组织事件信息，每个节点代表一个事件，节点之间的连接表示事件之间的关系。3) 更新策略：用于更新树结构，例如合并相似的事件、删除过时的事件等。细粒度时空窗口的关键设计包括：1) 窗口大小：用于控制捕捉短期视觉线索的范围。2) 特征融合方式：用于将短期视觉线索与长期记忆信息进行融合。

## 📊 实验亮点

StreamForest在多个基准测试中取得了显著的性能提升。在StreamingBench上，准确率达到77.3%；在OVBench上，准确率达到60.5%；在OVO-Bench上，准确率达到55.6%。更重要的是，即使在极端的视觉token压缩下（限制为1024个token），StreamForest相对于默认设置，在八个基准测试中仍保持了96.8%的平均准确率，充分证明了其鲁棒性和效率。

## 🎯 应用场景

StreamForest在自动驾驶、智能监控、视频会议等实时流式视频理解领域具有广泛的应用前景。它可以帮助自动驾驶系统更好地理解周围环境，提高驾驶安全性；可以帮助智能监控系统更准确地识别异常行为，提高安全防范能力；可以帮助视频会议系统更好地理解会议内容，提高沟通效率。未来，StreamForest有望成为实时视频理解领域的重要技术支撑。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have recently achieved remarkable progress in video understanding. However, their effectiveness in real-time streaming scenarios remains limited due to storage constraints of historical visual features and insufficient real-time spatiotemporal reasoning. To address these challenges, we propose StreamForest, a novel architecture specifically designed for streaming video understanding. Central to StreamForest is the Persistent Event Memory Forest, a memory mechanism that adaptively organizes video frames into multiple event-level tree structures. This process is guided by penalty functions based on temporal distance, content similarity, and merge frequency, enabling efficient long-term memory retention under limited computational resources. To enhance real-time perception, we introduce a Fine-grained Spatiotemporal Window, which captures detailed short-term visual cues to improve current scene perception. Additionally, we present OnlineIT, an instruction-tuning dataset tailored for streaming video tasks. OnlineIT significantly boosts MLLM performance in both real-time perception and future prediction. To evaluate generalization in practical applications, we introduce ODV-Bench, a new benchmark focused on real-time streaming video understanding in autonomous driving scenarios. Experimental results demonstrate that StreamForest achieves the state-of-the-art performance, with accuracies of 77.3% on StreamingBench, 60.5% on OVBench, and 55.6% on OVO-Bench. In particular, even under extreme visual token compression (limited to 1024 tokens), the model retains 96.8% of its average accuracy in eight benchmarks relative to the default setting. These results underscore the robustness, efficiency, and generalizability of StreamForest for streaming video understanding.

