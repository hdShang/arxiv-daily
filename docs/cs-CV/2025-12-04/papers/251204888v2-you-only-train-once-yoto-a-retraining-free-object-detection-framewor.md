---
layout: default
title: "You Only Train Once (YOTO): A Retraining-Free Object Detection Framework"
---

# You Only Train Once (YOTO): A Retraining-Free Object Detection Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04888" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04888v2</a>
  <a href="https://arxiv.org/pdf/2512.04888.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04888v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04888v2', 'You Only Train Once (YOTO): A Retraining-Free Object Detection Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Priyanto Hidayatullah, Nurjannah Syakrani, Yudi Widhiyasana, Muhammad Rizqi Sholahuddin, Refdinal Tubagus, Zahri Al Adzani Hidayat, Hanri Fajar Ramadhan, Dafa Alfarizki Pratama, Farhan Muhammad Yasin

**分类**: cs.CV

**发布日期**: 2025-12-04 (更新: 2025-12-05)

**备注**: This manuscript was first submitted to the Engineering (Elsevier Journal). The preprint version was posted to arXiv afterwards to facilitate open access and community feedback

---

## 💡 一句话要点

**提出YOTO框架，解决目标检测中免重训练的新品增量学习问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `目标检测` `增量学习` `免重训练` `度量学习` `零售应用` `灾难性遗忘` `YOLO` `边缘计算`

## 📋 核心要点

1. 目标检测面临灾难性遗忘问题，每次新增产品都需要重训练整个模型，耗时耗力。
2. YOTO框架结合YOLO11n进行定位，DeIT和Proxy Anchor Loss进行特征提取，并使用向量数据库进行分类。
3. 实验表明，YOTO在零售场景下无需重训练即可有效检测新旧产品，训练效率提升显著。

## 📝 摘要（中文）

本文提出了一种名为You Only Train Once (YOTO) 的框架，旨在解决目标检测中灾难性遗忘的问题。当引入新产品时，传统方法需要使用新产品数据集和完整旧数据集进行重训练，导致训练成本增加和时间消耗。YOTO通过结合YOLO11n进行目标定位，DeIT和Proxy Anchor Loss进行特征提取和度量学习来解决这个问题。分类阶段，使用目标产品和Qdrant向量数据库中特征向量的余弦相似度。在包含140种产品的零售店案例研究中，实验结果表明该框架在检测新产品和现有产品方面都取得了令人鼓舞的准确性。此外，无需重训练显著提高了训练效率，相比传统方法提升近3倍，并且随着新产品增加效率更高。在边缘设备上，每张包含多个产品的图像平均推理时间为580毫秒，验证了该框架的实际应用可行性。

## 🔬 方法详解

**问题定义**：目标检测模型在实际应用中，经常需要处理新增类别（例如零售场景中的新产品）。传统的做法是，每次新增类别，都需要使用包含新类别和旧类别的数据集重新训练整个模型。这种重训练的方式不仅耗费大量时间和计算资源，而且容易导致灾难性遗忘，即模型在学习新知识的同时忘记了旧知识。因此，如何实现免重训练的目标检测，即在不重新训练整个模型的情况下，快速适应新的类别，是一个重要的研究问题。

**核心思路**：YOTO框架的核心思路是解耦目标检测任务中的定位和分类两个子任务。对于定位任务，使用YOLO11n进行目标框的预测；对于分类任务，则采用度量学习的方式，将每个类别学习到一个特征向量空间中的嵌入表示。当需要识别新的类别时，只需要将新类别的特征向量添加到特征向量数据库中，而无需重新训练整个模型。

**技术框架**：YOTO框架主要包含以下几个模块：1) YOLO11n目标检测器：负责检测图像中的目标，并提取目标区域的特征。2) DeIT特征提取器：用于提取目标区域的视觉特征，并将其映射到特征向量空间中。3) Proxy Anchor Loss：用于训练特征提取器，使得同一类别的目标在特征向量空间中更加接近，不同类别的目标更加远离。4) Qdrant向量数据库：用于存储所有类别的特征向量。5) Cosine Similarity分类器：用于计算目标区域的特征向量与向量数据库中各个类别特征向量的余弦相似度，从而判断目标的类别。

**关键创新**：YOTO框架的关键创新在于将目标检测任务解耦为定位和分类两个子任务，并采用度量学习的方式进行分类。这种解耦的方式使得模型可以独立地学习新类别的特征，而无需重新训练整个模型。此外，使用Proxy Anchor Loss可以有效地提高特征向量的区分性，从而提高分类的准确率。

**关键设计**：在特征提取器方面，选择了DeIT模型，因为它具有较强的特征提取能力。在损失函数方面，选择了Proxy Anchor Loss，因为它能够有效地提高特征向量的区分性。在向量数据库方面，选择了Qdrant，因为它具有高效的向量检索能力。此外，还对YOLO11n进行了微调，以适应特定的目标检测任务。

## 📊 实验亮点

实验结果表明，YOTO框架在零售店的140种产品数据集上取得了令人鼓舞的准确性，无论是检测新产品还是现有产品。与传统的重训练方法相比，YOTO框架的训练时间效率提高了近3倍，并且随着新产品数量的增加，效率提升更加显著。此外，在边缘设备上，YOTO框架的平均推理时间为580毫秒/图像，验证了其在实际应用中的可行性。

## 🎯 应用场景

YOTO框架在零售、工业质检、智能安防等领域具有广泛的应用前景。例如，在零售场景中，可以快速添加新产品而无需重新训练模型，提高运营效率。在工业质检中，可以快速适应新的缺陷类型，提高检测精度。在智能安防中，可以快速识别新的目标，提高安全等级。该研究为解决目标检测中的灾难性遗忘问题提供了一种有效的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Object detection constitutes the primary task within the domain of computer vision. It is utilized in numerous domains. Nonetheless, object detection continues to encounter the issue of catastrophic forgetting. The model must be retrained whenever new products are introduced, utilizing not only the new products dataset but also the entirety of the previous dataset. The outcome is obvious: increasing model training expenses and significant time consumption. In numerous sectors, particularly retail checkout, the frequent introduction of new products presents a great challenge. This study introduces You Only Train Once (YOTO), a methodology designed to address the issue of catastrophic forgetting by integrating YOLO11n for object localization with DeIT and Proxy Anchor Loss for feature extraction and metric learning. For classification, we utilize cosine similarity between the embedding features of the target product and those in the Qdrant vector database. In a case study conducted in a retail store with 140 products, the experimental results demonstrate that our proposed framework achieves encouraging accuracy, whether for detecting new or existing products. Furthermore, without retraining, the training duration difference is significant. We achieve almost 3 times the training time efficiency compared to classical object detection approaches. This efficiency escalates as additional new products are added to the product database. The average inference time is 580 ms per image containing multiple products, on an edge device, validating the proposed framework's feasibility for practical use.

