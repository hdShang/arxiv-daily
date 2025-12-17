---
layout: default
title: Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain
---

# Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07029" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07029v1</a>
  <a href="https://arxiv.org/pdf/2511.07029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07029v1" onclick="toggleFavorite(this, '2511.07029v1', 'Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Zhou, Qiming Wang, Tianze Chen

**分类**: cs.CV

**发布日期**: 2025-11-10

**备注**: Accepted by AAAI26

---

## 💡 一句话要点

**FreqCert：提出频域认证框架，提升3D点云识别对L2范数扰动的鲁棒性**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `三维点云识别` `鲁棒性认证` `对抗扰动` `图傅里叶变换` `频域分析`

## 📋 核心要点

1. 现有3D点云分类器易受对抗扰动和几何畸变攻击，空间域防御方法难以应对改变整体结构的扰动。
2. FreqCert将鲁棒性分析转移到频域，通过图傅里叶变换和频率感知子采样，提升对L2范数扰动的鲁棒性。
3. 实验表明，FreqCert在ModelNet40和ScanObjectNN数据集上，实现了更高的认证准确率和经验准确率。

## 📝 摘要（中文）

三维点云分类是自动驾驶、机器人和增强现实等安全关键应用中的一项基本任务。然而，最近的研究表明，点云分类器容易受到结构化对抗扰动和几何畸变的影响，对其在安全关键场景中的部署构成风险。现有的认证防御限制了逐点扰动，但忽略了细微的几何畸变，这些畸变保留了单个点，但改变了整体结构，可能导致错误分类。本文提出了FreqCert，一种新颖的认证框架，它通过将鲁棒性分析转移到频域来摆脱传统的空间域防御，从而实现针对全局L2有界扰动的结构化认证。FreqCert首先通过图傅里叶变换（GFT）转换输入点云，然后应用结构化的频率感知子采样来生成多个子点云。每个子云由一个标准模型独立分类，最终预测通过多数投票获得，其中子云是基于频谱相似性而不是空间邻近性构建的，这使得分区在L2扰动下更稳定，并且更好地与对象的内在结构对齐。我们推导了认证L2鲁棒性半径的闭式下界，并在最小和可解释的假设下证明了其紧密性，为频域认证奠定了理论基础。在ModelNet40和ScanObjectNN数据集上的大量实验表明，FreqCert始终在强扰动下实现更高的认证准确率和经验准确率。我们的结果表明，频谱表示为三维点云识别中的可认证鲁棒性提供了一条有效的途径。

## 🔬 方法详解

**问题定义**：现有3D点云分类器容易受到对抗样本的攻击，尤其是在安全攸关的应用中。现有的认证防御方法主要集中在限制点级别的扰动，忽略了可能改变点云整体结构的几何畸变，这些畸变虽然保持了单个点的位置，但改变了点云的整体形状，导致分类错误。因此，如何有效地防御这种结构化的、全局的扰动是一个关键问题。

**核心思路**：FreqCert的核心思路是将点云的鲁棒性分析从空间域转移到频域。通过图傅里叶变换（GFT），将点云转换到频域表示，然后在频域进行结构化的子采样。这种方法的优势在于，频域表示能够更好地捕捉点云的全局结构信息，并且对L2范数扰动具有更强的抵抗能力。通过在频域进行操作，可以更有效地识别和过滤掉对抗扰动，从而提高分类器的鲁棒性。

**技术框架**：FreqCert的整体框架包括以下几个主要步骤：1) **图傅里叶变换（GFT）**：将输入的点云通过GFT转换到频域。2) **频率感知子采样**：在频域中，根据频谱相似性进行结构化的子采样，生成多个子点云。3) **独立分类**：每个子点云由一个标准的点云分类模型独立进行分类。4) **多数投票**：将所有子点云的分类结果进行多数投票，得到最终的分类结果。

**关键创新**：FreqCert的关键创新在于将鲁棒性认证问题转移到频域进行分析和解决。与传统的空间域防御方法不同，FreqCert利用图傅里叶变换将点云转换到频域，从而能够更好地捕捉点云的全局结构信息，并对结构化的扰动具有更强的抵抗能力。此外，FreqCert提出的频率感知子采样方法，能够根据频谱相似性生成多个子点云，进一步提高了分类器的鲁棒性。

**关键设计**：FreqCert的关键设计包括：1) **图傅里叶变换（GFT）的选择**：选择合适的GFT方法对于将点云有效地转换到频域至关重要。论文中可能使用了特定的GFT变体，并对其参数进行了优化。2) **频率感知子采样的策略**：如何根据频谱相似性进行子采样，以及子采样的数量和比例，是影响FreqCert性能的关键因素。3) **多数投票的策略**：如何有效地进行多数投票，例如是否考虑不同子点云的置信度，也是一个重要的设计考虑。

## 📊 实验亮点

FreqCert在ModelNet40和ScanObjectNN数据集上进行了广泛的实验，结果表明，FreqCert在强扰动下始终能够实现更高的认证准确率和经验准确率。具体来说，FreqCert在认证鲁棒性方面显著优于现有的空间域防御方法，并且在经验准确率方面也取得了可观的提升。这些实验结果表明，FreqCert是一种有效的3D点云鲁棒性认证方法。

## 🎯 应用场景

FreqCert在自动驾驶、机器人和增强现实等安全关键领域具有广泛的应用前景。它可以提高这些系统在面对恶意攻击或环境干扰时的可靠性和安全性。例如，在自动驾驶中，FreqCert可以防御对抗样本攻击，确保车辆能够准确识别交通标志和行人，从而避免交通事故。在机器人领域，它可以提高机器人在复杂环境中的感知能力，使其能够安全地执行任务。在增强现实领域，它可以提高虚拟物体的稳定性，增强用户体验。

## 📄 摘要（原文）

> 3D point cloud classification is a fundamental task in safety-critical applications such as autonomous driving, robotics, and augmented reality. However, recent studies reveal that point cloud classifiers are vulnerable to structured adversarial perturbations and geometric corruptions, posing risks to their deployment in safety-critical scenarios. Existing certified defenses limit point-wise perturbations but overlook subtle geometric distortions that preserve individual points yet alter the overall structure, potentially leading to misclassification. In this work, we propose FreqCert, a novel certification framework that departs from conventional spatial domain defenses by shifting robustness analysis to the frequency domain, enabling structured certification against global L2-bounded perturbations. FreqCert first transforms the input point cloud via the graph Fourier transform (GFT), then applies structured frequency-aware subsampling to generate multiple sub-point clouds. Each sub-cloud is independently classified by a standard model, and the final prediction is obtained through majority voting, where sub-clouds are constructed based on spectral similarity rather than spatial proximity, making the partitioning more stable under L2 perturbations and better aligned with the object's intrinsic structure. We derive a closed-form lower bound on the certified L2 robustness radius and prove its tightness under minimal and interpretable assumptions, establishing a theoretical foundation for frequency domain certification. Extensive experiments on the ModelNet40 and ScanObjectNN datasets demonstrate that FreqCert consistently achieves higher certified accuracy and empirical accuracy under strong perturbations. Our results suggest that spectral representations provide an effective pathway toward certifiable robustness in 3D point cloud recognition.

