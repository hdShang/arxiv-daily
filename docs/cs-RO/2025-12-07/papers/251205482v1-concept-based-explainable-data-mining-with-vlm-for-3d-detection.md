---
layout: default
title: Concept-based Explainable Data Mining with VLM for 3D Detection
---

# Concept-based Explainable Data Mining with VLM for 3D Detection

**arXiv**: [2512.05482v1](https://arxiv.org/abs/2512.05482) | [PDF](https://arxiv.org/pdf/2512.05482.pdf)

**作者**: Mai Tsujimoto

---

## 💡 一句话要点

**提出基于概念的可解释数据挖掘框架，利用2D视觉语言模型提升自动驾驶中3D罕见物体检测性能。**

**关键词**: `3D物体检测` `视觉语言模型` `数据挖掘` `异常检测` `自动驾驶` `概念解释`

## 📋 核心要点

1. 核心问题：自动驾驶中仅依赖点云数据时，罕见物体检测仍具挑战性，现有方法未充分利用视觉语言模型的潜力。
2. 方法要点：结合目标检测、语义特征提取、降维和多方面异常检测，通过概念过滤识别语义上有意义的罕见物体，减少标注负担。
3. 实验或效果：在nuScenes数据集上验证，该策略仅用少量训练数据即提升3D检测模型性能，对拖车和自行车等类别改进显著。

## 📄 摘要（原文）

> Rare-object detection remains a challenging task in autonomous driving systems, particularly when relying solely on point cloud data. Although Vision-Language Models (VLMs) exhibit strong capabilities in image understanding, their potential to enhance 3D object detection through intelligent data mining has not been fully explored. This paper proposes a novel cross-modal framework that leverages 2D VLMs to identify and mine rare objects from driving scenes, thereby improving 3D object detection performance. Our approach synthesizes complementary techniques such as object detection, semantic feature extraction, dimensionality reduction, and multi-faceted outlier detection into a cohesive, explainable pipeline that systematically identifies rare but critical objects in driving scenes. By combining Isolation Forest and t-SNE-based outlier detection methods with concept-based filtering, the framework effectively identifies semantically meaningful rare objects. A key strength of this approach lies in its ability to extract and annotate targeted rare object concepts such as construction vehicles, motorcycles, and barriers. This substantially reduces the annotation burden and focuses only on the most valuable training samples. Experiments on the nuScenes dataset demonstrate that this concept-guided data mining strategy enhances the performance of 3D object detection models while utilizing only a fraction of the training data, with particularly notable improvements for challenging object categories such as trailers and bicycles compared with the same amount of random data. This finding has substantial implications for the efficient curation of datasets in safety-critical autonomous systems.

