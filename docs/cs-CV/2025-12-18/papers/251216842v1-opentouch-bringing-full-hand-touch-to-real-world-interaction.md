---
layout: default
title: "OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction"
---

# OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16842" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16842v1</a>
  <a href="https://arxiv.org/pdf/2512.16842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16842v1', 'OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Ray Song, Jinzhou Li, Rao Fu, Devin Murphy, Kaichen Zhou, Rishi Shiv, Yaqi Li, Haoyu Xiong, Crystal Elaine Owens, Yilun Du, Yiyue Luo, Xianyi Cheng, Antonio Torralba, Wojciech Matusik, Paul Pu Liang

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-12-18

**备注**: https://opentouch-tactile.github.io/

---

## 💡 一句话要点

**OPENTOUCH：构建真实场景下全手触觉交互数据集与基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全手触觉` `自我中心视觉` `多模态数据集` `具身智能` `机器人操作` `触觉感知` `跨模态学习`

## 📋 核心要点

1. 现有方法缺乏在真实场景下同步第一人称视频与全手触觉的数据集，阻碍了视觉与触觉融合研究。
2. OpenTouch数据集包含同步的视频、触觉和姿势数据，并提供检索和分类基准，用于评估触觉在感知和行动中的作用。
3. 实验表明，触觉信号能有效提升抓取理解和跨模态对齐，并可从视频中可靠检索触觉信息。

## 📝 摘要（中文）

人手是与物理世界交互的主要界面，但自我中心感知很少知道何时、何地或以多大力度进行接触。目前缺乏稳健的可穿戴触觉传感器，并且没有现有的真实场景数据集将第一人称视频与全手触觉对齐。为了弥合视觉感知和物理交互之间的差距，我们提出了OpenTouch，这是第一个真实场景下的自我中心全手触觉数据集，包含5.1小时的同步视频-触觉-姿势数据和2,900个带有详细文本注释的精选片段。利用OpenTouch，我们引入了检索和分类基准，以探索触觉如何支撑感知和行动。我们表明，触觉信号为抓取理解提供了一个紧凑而强大的线索，加强了跨模态对齐，并且可以从真实场景视频查询中可靠地检索。通过发布这个带注释的视觉-触觉-姿势数据集和基准，我们的目标是推进多模态自我中心感知、具身学习和富含接触的机器人操作。

## 🔬 方法详解

**问题定义**：现有方法缺乏在真实场景下同步第一人称视频与全手触觉的数据集，导致无法有效研究视觉和触觉的融合，限制了具身智能和机器人操作的发展。现有可穿戴触觉传感器不够鲁棒，难以在真实场景中应用。

**核心思路**：论文的核心思路是通过构建一个大规模的、带注释的真实场景全手触觉数据集，为多模态自我中心感知提供数据基础。通过设计检索和分类基准，鼓励研究者探索触觉在感知和行动中的作用，并评估不同模型的性能。

**技术框架**：OpenTouch数据集包含同步的自我中心视频、全手触觉数据和手部姿势数据。数据采集过程涉及多种真实场景下的交互任务。数据集还包含2900个带有详细文本注释的精选片段。基于该数据集，论文提出了两个基准任务：触觉检索和触觉分类。触觉检索任务旨在从视频中检索对应的触觉信号，触觉分类任务旨在根据触觉信号识别交互动作。

**关键创新**：该论文的关键创新在于构建了首个真实场景下的自我中心全手触觉数据集，并提出了相应的检索和分类基准。该数据集的规模和质量为多模态感知研究提供了新的资源。此外，论文还展示了触觉信号在抓取理解和跨模态对齐方面的潜力。

**关键设计**：数据集采集过程中，使用了可穿戴触觉传感器来获取全手触觉信息，并使用同步设备记录自我中心视频和手部姿势数据。为了保证数据的质量，论文对数据进行了清洗和标注。在基准任务中，论文使用了标准的深度学习模型，并针对触觉数据的特点进行了优化。具体的参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，触觉信号能够显著提升抓取理解的准确率，并加强跨模态对齐的效果。在触觉检索任务中，模型能够从真实场景视频中可靠地检索出对应的触觉信号。这些结果验证了触觉在感知和行动中的重要作用，并为未来的研究提供了有力的支持。

## 🎯 应用场景

OpenTouch数据集和基准可应用于机器人操作、具身智能、人机交互等领域。例如，可以训练机器人通过触觉感知来更好地理解和执行抓取任务，或者开发更自然的人机交互界面，使用户可以通过触摸与虚拟环境进行交互。该研究有望推动机器人更加智能和自主，并改善人机交互体验。

## 📄 摘要（原文）

> The human hand is our primary interface to the physical world, yet egocentric perception rarely knows when, where, or how forcefully it makes contact. Robust wearable tactile sensors are scarce, and no existing in-the-wild datasets align first-person video with full-hand touch. To bridge the gap between visual perception and physical interaction, we present OpenTouch, the first in-the-wild egocentric full-hand tactile dataset, containing 5.1 hours of synchronized video-touch-pose data and 2,900 curated clips with detailed text annotations. Using OpenTouch, we introduce retrieval and classification benchmarks that probe how touch grounds perception and action. We show that tactile signals provide a compact yet powerful cue for grasp understanding, strengthen cross-modal alignment, and can be reliably retrieved from in-the-wild video queries. By releasing this annotated vision-touch-pose dataset and benchmark, we aim to advance multimodal egocentric perception, embodied learning, and contact-rich robotic manipulation.

