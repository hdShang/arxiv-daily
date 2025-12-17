---
layout: default
title: RISE: Single Static Radar-based Indoor Scene Understanding
---

# RISE: Single Static Radar-based Indoor Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14019" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14019v1</a>
  <a href="https://arxiv.org/pdf/2511.14019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14019v1" onclick="toggleFavorite(this, '2511.14019v1', 'RISE: Single Static Radar-based Indoor Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaichen Zhou, Laura Dodds, Sayed Saad Afzal, Fadel Adib

**分类**: cs.CV

**发布日期**: 2025-11-18

---

## 💡 一句话要点

**RISE：基于单静态雷达的室内场景理解，利用多径反射提升几何推理能力**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `雷达` `室内场景理解` `多径反射` `目标检测` `布局重建` `毫米波雷达` `几何推理`

## 📋 核心要点

1. 现有室内场景理解方法依赖光学传感器，易受遮挡影响且存在隐私泄露风险，而雷达虽能穿透障碍物，但分辨率低，几何推理困难。
2. RISE通过显式建模到达角和离开角，增强多径反射信息，恢复隐藏结构，从而提升雷达的几何感知能力。
3. RISE构建了大规模雷达室内场景数据集，实验表明，其布局重建精度提升显著，并首次实现了基于毫米波雷达的目标检测。

## 📝 摘要（中文）

鲁棒且保护隐私的室内场景理解仍然是一个根本性的开放问题。虽然RGB和LiDAR等光学传感器提供高空间保真度，但它们存在严重的遮挡，并在室内环境中引入隐私风险。相比之下，毫米波(mmWave)雷达保护隐私并穿透障碍物，但其固有的低空间分辨率使得可靠的几何推理变得困难。我们介绍了RISE，这是第一个用于单静态雷达室内场景理解的基准和系统，共同针对布局重建和目标检测。RISE建立在多径反射编码丰富几何线索的关键洞察之上，传统上多径反射被视为噪声。为此，我们提出了一种双角度多径增强方法，该方法显式地建模到达角和离开角，以恢复二次（幽灵）反射并揭示不可见的结构。在这些增强的观测之上，一个模拟到现实的分层扩散框架将碎片化的雷达响应转换为完整的布局重建和目标检测。我们的基准包含在100个真实室内轨迹中收集的50,000帧，形成了第一个专用于基于雷达的室内场景理解的大规模数据集。大量实验表明，与最先进的布局重建相比，RISE将Chamfer距离降低了60%（降至16厘米），并提供了第一个基于毫米波的目标检测，实现了58%的IoU。这些结果将RISE确立为使用单个静态雷达进行几何感知和保护隐私的室内场景理解的新基础。

## 🔬 方法详解

**问题定义**：论文旨在解决单静态雷达在室内场景理解中几何推理能力不足的问题。现有方法难以有效利用雷达数据中的多径反射信息，导致布局重建精度低，无法进行可靠的目标检测。传统方法通常将多径反射视为噪声进行滤除，忽略了其中蕴含的丰富几何信息。

**核心思路**：论文的核心思路是充分利用雷达信号中的多径反射信息，将其视为一种几何线索，而非噪声。通过精确建模信号的到达角(Angle-of-Arrival, AoA)和离开角(Angle-of-Departure, AoD)，可以恢复由于遮挡而不可见的场景结构，从而提升雷达的几何感知能力。

**技术框架**：RISE的整体框架包含两个主要阶段：首先是双角度多径增强(Bi-Angular Multipath Enhancement)，用于提取和增强多径反射信息；然后是模拟到现实的分层扩散框架(Simulation-to-Reality Hierarchical Diffusion)，用于将增强后的雷达响应转化为完整的布局重建和目标检测结果。该框架利用仿真数据进行预训练，然后通过迁移学习适应真实雷达数据。

**关键创新**：RISE的关键创新在于双角度多径增强模块，它显式地建模了雷达信号的AoA和AoD，从而能够有效地恢复二次反射（ghost reflections），揭示被遮挡的场景结构。与传统方法直接滤除多径反射不同，RISE将其作为一种有用的几何信息加以利用。

**关键设计**：双角度多径增强模块使用专门设计的网络结构来预测每个雷达信号的AoA和AoD。分层扩散框架采用多尺度特征提取和扩散过程，逐步将碎片化的雷达响应转化为完整的场景表示。损失函数包括布局重建损失和目标检测损失，并采用对抗训练来提高模型的鲁棒性。

## 📊 实验亮点

RISE在布局重建任务中，相较于现有技术，将Chamfer距离降低了60%，达到了16厘米的精度。此外，RISE首次实现了基于毫米波雷达的目标检测，取得了58%的IoU。这些结果表明，RISE在雷达室内场景理解方面具有显著的优势，为后续研究奠定了基础。

## 🎯 应用场景

RISE技术可应用于智能家居、机器人导航、安防监控等领域。通过利用雷达的隐私保护和穿透能力，可以在不侵犯个人隐私的前提下，实现对室内环境的全面感知和理解。该技术还有助于提升机器人在复杂环境中的自主导航能力，并为智能安防系统提供更可靠的感知数据。

## 📄 摘要（原文）

> Robust and privacy-preserving indoor scene understanding remains a fundamental open problem. While optical sensors such as RGB and LiDAR offer high spatial fidelity, they suffer from severe occlusions and introduce privacy risks in indoor environments. In contrast, millimeter-wave (mmWave) radar preserves privacy and penetrates obstacles, but its inherently low spatial resolution makes reliable geometric reasoning difficult.
>   We introduce RISE, the first benchmark and system for single-static-radar indoor scene understanding, jointly targeting layout reconstruction and object detection. RISE is built upon the key insight that multipath reflections, traditionally treated as noise, encode rich geometric cues. To exploit this, we propose a Bi-Angular Multipath Enhancement that explicitly models Angle-of-Arrival and Angle-of-Departure to recover secondary (ghost) reflections and reveal invisible structures. On top of these enhanced observations, a simulation-to-reality Hierarchical Diffusion framework transforms fragmented radar responses into complete layout reconstruction and object detection.
>   Our benchmark contains 50,000 frames collected across 100 real indoor trajectories, forming the first large-scale dataset dedicated to radar-based indoor scene understanding. Extensive experiments show that RISE reduces the Chamfer Distance by 60% (down to 16 cm) compared to the state of the art in layout reconstruction, and delivers the first mmWave-based object detection, achieving 58% IoU. These results establish RISE as a new foundation for geometry-aware and privacy-preserving indoor scene understanding using a single static radar.

