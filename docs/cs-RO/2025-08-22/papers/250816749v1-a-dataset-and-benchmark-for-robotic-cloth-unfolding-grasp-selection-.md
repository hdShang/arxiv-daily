---
layout: default
title: "A Dataset and Benchmark for Robotic Cloth Unfolding Grasp Selection: The ICRA 2024 Cloth Competition"
---

# A Dataset and Benchmark for Robotic Cloth Unfolding Grasp Selection: The ICRA 2024 Cloth Competition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16749" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16749v1</a>
  <a href="https://arxiv.org/pdf/2508.16749.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16749v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16749v1', 'A Dataset and Benchmark for Robotic Cloth Unfolding Grasp Selection: The ICRA 2024 Cloth Competition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Victor-Louis De Gusseme, Thomas Lips, Remko Proesmans, Julius Hietala, Giwan Lee, Jiyoung Choi, Jeongil Choi, Geon Kim, Phayuth Yonrith, Domen Tabernik, Andrej Gams, Peter Nimac, Matej Urbas, Jon Muhovič, Danijel Skočaj, Matija Mavsar, Hyojeong Yu, Minseo Kwon, Young J. Kim, Yang Cong, Ronghan Chen, Yu Ren, Supeng Diao, Jiawei Weng, Jiayue Liu, Haoran Sun, Linhan Yang, Zeqing Zhang, Ning Guo, Lei Yang, Fang Wan, Chaoyang Song, Jia Pan, Yixiang Jin, Yong A, Jun Shi, Dingzhe Li, Yong Yang, Kakeru Yamasaki, Takumi Kajiwara, Yuki Nakadera, Krati Saxena, Tomohiro Shibata, Chongkun Xia, Kai Mo, Yanzhao Yu, Qihao Lin, Binqiang Ma, Uihun Sagong, JungHyun Choi, JeongHyun Park, Dongwoo Lee, Yeongmin Kim, Myun Joong Hwang, Yusuke Kuribayashi, Naoki Hiratsuka, Daisuke Tanaka, Solvi Arnold, Kimitoshi Yamazaki, Carlos Mateo-Agullo, Andreas Verleysen, Francis Wyffels

**分类**: cs.RO

**发布日期**: 2025-08-22

**备注**: submitted to IJRR

---

## 💡 一句话要点

**提出机器人布料展开抓取选择基准以解决评估不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操控` `布料展开` `抓取选择` `数据集` `基准评估` `ICRA 2024` `手工设计方法`

## 📋 核心要点

1. 现有的机器人布料操控方法缺乏标准化的基准和共享数据集，导致评估和比较困难。
2. 论文提出了一个新的基准和数据集，并通过ICRA 2024布料竞赛进行抓取姿态选择的评估。
3. 竞赛结果显示手工设计方法表现出色，并揭示了抓取成功率与覆盖率之间的权衡，强调了独立评估的重要性。

## 📝 摘要（中文）

机器人布料操控面临缺乏标准化基准和共享数据集的问题，限制了不同方法的评估与比较。为此，研究团队创建了一个基准，并组织了ICRA 2024布料竞赛，专注于空中布料展开的抓取姿态选择。共有11个多样化团队参与，利用公开发布的数据集进行展开方法设计。竞赛结果分析揭示了抓取成功率与覆盖率之间的权衡，手工设计方法的强大表现，以及竞赛表现与以往工作的显著差异，强调了独立实验评估的重要性。该数据集为抓取选择方法的开发与评估提供了宝贵资源，尤其是学习型方法。希望本基准、数据集和竞赛结果能为未来的基准奠定基础，推动数据驱动的机器人布料操控进展。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人布料操控中缺乏标准化评估基准和共享数据集的问题，现有方法在评估和比较上存在不足。

**核心思路**：通过创建一个新的基准和数据集，并组织ICRA 2024布料竞赛，集中评估抓取姿态选择的有效性，推动该领域的发展。

**技术框架**：整体架构包括数据集的构建、竞赛的组织以及结果的分析。数据集包含679个展开演示，涵盖34种服装，竞赛则通过多样化的方法进行抓取姿态选择的评估。

**关键创新**：最重要的创新在于创建了一个公开的数据集和基准，促进了不同方法的比较与评估，特别是强调了手工设计方法在实际应用中的强大表现。

**关键设计**：数据集包含176个竞赛评估试验，采用多种方法进行抓取姿态选择，分析了抓取成功率与覆盖率的权衡，提供了对比基线和性能数据。具体的参数设置和损失函数等技术细节在论文中进行了详细描述。

## 📊 实验亮点

竞赛结果显示，手工设计方法在抓取成功率和覆盖率之间取得了良好的平衡，表现出色。与以往研究相比，竞赛表现的显著差异强调了独立评估的重要性，为未来的研究提供了新的视角和方向。

## 🎯 应用场景

该研究的潜在应用领域包括机器人布料操控、智能家居和自动化服装处理等。通过提供标准化的评估基准和数据集，研究成果能够推动相关领域的技术进步，促进机器人在复杂环境中的操作能力提升。

## 📄 摘要（原文）

> Robotic cloth manipulation suffers from a lack of standardized benchmarks and shared datasets for evaluating and comparing different approaches. To address this, we created a benchmark and organized the ICRA 2024 Cloth Competition, a unique head-to-head evaluation focused on grasp pose selection for in-air robotic cloth unfolding. Eleven diverse teams participated in the competition, utilizing our publicly released dataset of real-world robotic cloth unfolding attempts and a variety of methods to design their unfolding approaches. Afterwards, we also expanded our dataset with 176 competition evaluation trials, resulting in a dataset of 679 unfolding demonstrations across 34 garments. Analysis of the competition results revealed insights about the trade-off between grasp success and coverage, the surprisingly strong achievements of hand-engineered methods and a significant discrepancy between competition performance and prior work, underscoring the importance of independent, out-of-the-lab evaluation in robotic cloth manipulation. The associated dataset is a valuable resource for developing and evaluating grasp selection methods, particularly for learning-based approaches. We hope that our benchmark, dataset and competition results can serve as a foundation for future benchmarks and drive further progress in data-driven robotic cloth manipulation. The dataset and benchmarking code are available at https://airo.ugent.be/cloth_competition.

