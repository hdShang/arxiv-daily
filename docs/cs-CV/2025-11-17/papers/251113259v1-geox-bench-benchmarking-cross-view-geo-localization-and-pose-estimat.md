---
layout: default
title: GeoX-Bench: Benchmarking Cross-View Geo-Localization and Pose Estimation Capabilities of Large Multimodal Models
---

# GeoX-Bench: Benchmarking Cross-View Geo-Localization and Pose Estimation Capabilities of Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13259" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13259v1</a>
  <a href="https://arxiv.org/pdf/2511.13259.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13259v1" onclick="toggleFavorite(this, '2511.13259v1', 'GeoX-Bench: Benchmarking Cross-View Geo-Localization and Pose Estimation Capabilities of Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yushuo Zheng, Jiangyong Ying, Huiyu Duan, Chunyi Li, Zicheng Zhang, Jing Liu, Xiaohong Liu, Guangtao Zhai

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-17

**🔗 代码/项目**: [GITHUB](https://github.com/IntMeGroup/GeoX-Bench)

---

## 💡 一句话要点

**GeoX-Bench：用于评估大模型跨视角地理定位与姿态估计能力的基准测试。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `跨视角地理定位` `姿态估计` `大型多模态模型` `基准测试` `指令调优`

## 📋 核心要点

1. 现有大型多模态模型在跨视角地理定位和姿态估计方面的能力尚待探索，限制了其在导航等领域的应用。
2. GeoX-Bench通过构建包含全景-卫星图像对和问答对的综合基准，为评估和提升LMMs的地理定位能力提供了平台。
3. 实验表明，现有LMMs在地理定位任务中表现良好，但在姿态估计方面仍有不足，指令调优可以显著提升其跨视角地理感知能力。

## 📝 摘要（中文）

大型多模态模型(LMMs)在各种任务中表现出卓越的能力，但它们在跨视角地理定位和姿态估计领域的知识和能力仍未被探索，尽管这些能力对导航、自动驾驶、户外机器人等领域具有潜在的好处。为了弥补这一差距，我们推出了GeoX-Bench，这是一个综合基准，旨在探索和评估LMMs在跨视角地理定位和姿态估计方面的能力。具体来说，GeoX-Bench包含10,859个全景-卫星图像对，覆盖49个国家的128个城市，以及相应的755,976个问答(QA)对。其中，42,900个QA对被指定用于基准测试，其余的旨在增强LMMs的能力。基于GeoX-Bench，我们评估了25个最先进的LMMs在跨视角地理定位和姿态估计任务上的能力，并进一步探索了指令调优所赋予的能力。我们的基准测试表明，虽然当前的LMMs在地理定位任务中取得了令人印象深刻的性能，但它们在更复杂的姿态估计任务上的有效性显著下降，这突出了未来改进的关键领域，并且在GeoX-Bench的训练数据上进行指令调优可以显著提高跨视角地理感知能力。GeoX-Bench可在https://github.com/IntMeGroup/GeoX-Bench上获取。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在跨视角地理定位和姿态估计方面的能力评估问题。现有方法缺乏专门针对该领域设计的基准测试，难以有效评估和提升LMMs的地理感知能力。现有LMMs在复杂地理场景下的定位精度和姿态估计能力有待提高。

**核心思路**：论文的核心思路是构建一个包含大量真实世界数据的综合基准测试集GeoX-Bench，用于系统地评估LMMs在跨视角地理定位和姿态估计方面的性能。通过提供多样化的全景-卫星图像对和问答对，GeoX-Bench能够全面考察LMMs的地理知识和推理能力。同时，利用该基准进行指令调优，进一步提升LMMs的地理感知能力。

**技术框架**：GeoX-Bench主要包含以下几个部分：
1.  **数据集构建**：收集并整理了来自全球多个城市的全景图像和对应的卫星图像，构建了包含10,859个图像对的数据集。
2.  **问答对生成**：为每个图像对生成了多个问答对，涵盖地理定位和姿态估计等多个方面，总计755,976个问答对。
3.  **基准测试**：选取42,900个问答对作为基准测试集，用于评估LMMs的性能。
4.  **模型评估**：使用基准测试集评估了25个最先进的LMMs，并分析了它们的优缺点。
5.  **指令调优**：利用GeoX-Bench的数据集对LMMs进行指令调优，提升其地理感知能力。

**关键创新**：GeoX-Bench的关键创新在于：
1.  **首个专门针对跨视角地理定位和姿态估计的LMMs基准测试**：填补了该领域的空白，为研究人员提供了一个统一的评估平台。
2.  **大规模、多样化的数据集**：包含来自全球多个城市的数据，能够全面评估LMMs的泛化能力。
3.  **问答对形式的评估方式**：能够更有效地考察LMMs的地理知识和推理能力。

**关键设计**：GeoX-Bench的关键设计包括：
1.  **数据集的地理多样性**：确保数据集包含来自不同地理区域和城市的数据，以评估LMMs的泛化能力。
2.  **问答对的类型多样性**：设计了多种类型的问答对，涵盖地理定位、姿态估计、地标识别等多个方面，以全面评估LMMs的地理感知能力。
3.  **评估指标的选择**：选择了合适的评估指标，如定位精度、姿态估计误差等，以客观地评估LMMs的性能。

## 📊 实验亮点

实验结果表明，现有LMMs在地理定位任务中表现出一定的能力，但在姿态估计任务中性能显著下降。通过在GeoX-Bench数据集上进行指令调优，LMMs的跨视角地理感知能力得到了显著提升，验证了该基准测试的有效性和价值。具体性能提升数据未知。

## 🎯 应用场景

该研究成果可广泛应用于导航、自动驾驶、户外机器人等领域。通过提升LMMs的跨视角地理定位和姿态估计能力，可以提高自动驾驶车辆的定位精度和环境感知能力，增强机器人在复杂环境中的导航能力，并为虚拟现实和增强现实应用提供更精确的地理信息。

## 📄 摘要（原文）

> Large multimodal models (LMMs) have demonstrated remarkable capabilities across a wide range of tasks, however their knowledge and abilities in the cross-view geo-localization and pose estimation domains remain unexplored, despite potential benefits for navigation, autonomous driving, outdoor robotics, \textit{etc}. To bridge this gap, we introduce \textbf{GeoX-Bench}, a comprehensive \underline{Bench}mark designed to explore and evaluate the capabilities of LMMs in \underline{cross}-view \underline{Geo}-localization and pose estimation. Specifically, GeoX-Bench contains 10,859 panoramic-satellite image pairs spanning 128 cities in 49 countries, along with corresponding 755,976 question-answering (QA) pairs. Among these, 42,900 QA pairs are designated for benchmarking, while the remaining are intended to enhance the capabilities of LMMs. Based on GeoX-Bench, we evaluate the capabilities of 25 state-of-the-art LMMs on cross-view geo-localization and pose estimation tasks, and further explore the empowered capabilities of instruction-tuning. Our benchmark demonstrate that while current LMMs achieve impressive performance in geo-localization tasks, their effectiveness declines significantly on the more complex pose estimation tasks, highlighting a critical area for future improvement, and instruction-tuning LMMs on the training data of GeoX-Bench can significantly improve the cross-view geo-sense abilities. The GeoX-Bench is available at \textcolor{magenta}{https://github.com/IntMeGroup/GeoX-Bench}.

