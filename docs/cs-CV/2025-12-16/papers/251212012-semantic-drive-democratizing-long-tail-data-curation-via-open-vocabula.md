---
layout: default
title: Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus
---

# Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12012" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12012</a>
  <a href="https://arxiv.org/pdf/2512.12012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12012" onclick="toggleFavorite(this, '2512.12012', 'Semantic-Drive: Democratizing Long-Tail Data Curation via Open-Vocabulary Grounding and Neuro-Symbolic VLM Consensus')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonio Guillen-Perez

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Semantic-Drive：通过开放词汇 grounding 和神经符号 VLM 共识实现长尾数据挖掘**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `长尾数据挖掘` `开放词汇检测` `视觉语言模型` `神经符号推理` `多模型共识` `本地部署`

## 📋 核心要点

1. 自动驾驶长尾数据匮乏，人工标注成本高昂，现有元数据搜索精度不足，云端VLM方案存在隐私和成本问题。
2. Semantic-Drive 采用本地优先的神经符号框架，通过开放词汇检测器和推理 VLM 实现语义数据挖掘。
3. 实验表明，Semantic-Drive 在 nuScenes 数据集上实现了更高的召回率，并显著降低了风险评估误差，且可在消费级硬件上运行。

## 📝 摘要（中文）

自动驾驶车辆(AVs)的稳健发展受到“长尾”训练数据稀缺的限制。虽然车队收集了PB级的视频日志，但识别罕见的安全关键事件(例如，不稳定的乱穿马路、施工改道)仍然是一个手动且成本高昂的过程。现有的解决方案依赖于粗略的元数据搜索(缺乏精度)或基于云的VLM(侵犯隐私且昂贵)。我们引入了Semantic-Drive，这是一个用于语义数据挖掘的本地优先、神经符号框架。我们的方法将感知解耦为两个阶段：(1)通过实时开放词汇检测器(YOLOE)进行符号 grounding 以锚定注意力，以及(2)通过推理VLM进行认知分析，执行取证场景分析。为了减轻幻觉，我们实现了一种“系统2”推理时对齐策略，利用多模型“Judge-Scout”共识机制。在nuScenes数据集上针对Waymo开放数据集(WOD-E2E)分类法进行基准测试，Semantic-Drive实现了0.966的召回率(CLIP为0.475)，并且与最佳单 scout 模型相比，风险评估误差降低了40%。该系统完全在消费级硬件(NVIDIA RTX 3090)上运行，为云提供了一种保护隐私的替代方案。

## 🔬 方法详解

**问题定义**：自动驾驶领域中，长尾场景数据（如罕见交通事件）的获取成本高昂，严重制约了自动驾驶系统的鲁棒性。现有方法依赖粗糙的元数据搜索，精度不足；而云端视觉语言模型（VLM）方案存在隐私泄露和高昂计算成本的风险。因此，如何高效、低成本、保护隐私地挖掘长尾数据是亟待解决的问题。

**核心思路**：Semantic-Drive 的核心思路是将复杂的场景理解任务分解为两个阶段：首先，利用开放词汇检测器进行符号 grounding，将视觉信息与语义概念关联；然后，利用推理 VLM 对场景进行认知分析，判断是否存在目标事件。此外，为了降低 VLM 的幻觉问题，引入了多模型共识机制，提高判断的可靠性。

**技术框架**：Semantic-Drive 包含以下主要模块：1) **开放词汇检测器 (YOLOE)**：用于检测图像中的物体，并将其与开放词汇表中的概念关联，实现符号 grounding。2) **推理 VLM**：对场景进行认知分析，判断是否存在目标事件。3) **Judge-Scout 共识机制**：采用多个 VLM 模型（Scout）进行独立判断，然后由一个 Judge 模型综合评估，形成最终的判断结果。这种多模型共识机制可以有效降低 VLM 的幻觉问题。

**关键创新**：Semantic-Drive 的关键创新在于：1) 提出了一个本地优先的神经符号框架，能够在消费级硬件上运行，保护用户隐私。2) 引入了 Judge-Scout 共识机制，有效降低了 VLM 的幻觉问题，提高了判断的可靠性。3) 将场景理解任务分解为符号 grounding 和认知分析两个阶段，降低了任务的复杂度。

**关键设计**：YOLOE 作为开放词汇检测器，其训练数据和检测精度至关重要。推理 VLM 的选择需要兼顾推理能力和计算效率。Judge-Scout 共识机制中，Scout 模型的数量和 Judge 模型的选择会影响最终的判断结果。论文中具体使用的 VLM 模型和参数设置未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12012/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12012/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12012/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Semantic-Drive 在 nuScenes 数据集上进行了评估，结果表明，其召回率达到 0.966，远高于 CLIP 的 0.475。与最佳单 Scout 模型相比，风险评估误差降低了 40%。该系统完全在消费级硬件（NVIDIA RTX 3090）上运行，验证了其在实际应用中的可行性。

## 🎯 应用场景

Semantic-Drive 可应用于自动驾驶长尾数据挖掘、智能交通监控、安全事件检测等领域。该系统能够帮助自动驾驶公司更高效地获取安全关键数据，提高自动驾驶系统的鲁棒性。同时，本地优先的设计使其能够在保护用户隐私的前提下进行数据分析，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> The development of robust Autonomous Vehicles (AVs) is bottlenecked by the scarcity of "Long-Tail" training data. While fleets collect petabytes of video logs, identifying rare safety-critical events (e.g., erratic jaywalking, construction diversions) remains a manual, cost-prohibitive process. Existing solutions rely on coarse metadata search, which lacks precision, or cloud-based VLMs, which are privacy-invasive and expensive. We introduce Semantic-Drive, a local-first, neuro-symbolic framework for semantic data mining. Our approach decouples perception into two stages: (1) Symbolic Grounding via a real-time open-vocabulary detector (YOLOE) to anchor attention, and (2) Cognitive Analysis via a Reasoning VLM that performs forensic scene analysis. To mitigate hallucination, we implement a "System 2" inference-time alignment strategy, utilizing a multi-model "Judge-Scout" consensus mechanism. Benchmarked on the nuScenes dataset against the Waymo Open Dataset (WOD-E2E) taxonomy, Semantic-Drive achieves a Recall of 0.966 (vs. 0.475 for CLIP) and reduces Risk Assessment Error by 40% ccompared to the best single scout models. The system runs entirely on consumer hardware (NVIDIA RTX 3090), offering a privacy-preserving alternative to the cloud.

