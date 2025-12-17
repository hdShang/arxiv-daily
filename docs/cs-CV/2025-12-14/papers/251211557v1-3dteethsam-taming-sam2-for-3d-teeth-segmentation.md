---
layout: default
title: 3DTeethSAM: Taming SAM2 for 3D Teeth Segmentation
---

# 3DTeethSAM: Taming SAM2 for 3D Teeth Segmentation

**arXiv**: [2512.11557v1](https://arxiv.org/abs/2512.11557) | [PDF](https://arxiv.org/pdf/2512.11557.pdf)

**作者**: Zhiguo Lu, Jianwen Lou, Mingjun Ma, Hairong Jin, Youyi Zheng, Kun Zhou

---

## 💡 一句话要点

**提出3DTeethSAM以解决3D牙齿分割问题，通过适配SAM2并引入轻量模块提升性能。**

**关键词**: `3D牙齿分割` `SAM2适配` `轻量模块` `2D-3D投影` `数字牙科` `基准测试`

## 📋 核心要点

1. 核心问题：3D牙齿分割在数字牙科中因真实牙列复杂性而具挑战性，需定位实例并语义分类。
2. 方法要点：从预定义视图渲染3D牙齿模型图像，应用SAM2进行2D分割，通过2D-3D投影重建结果，并引入提示嵌入生成器、掩码精炼器和分类器等轻量模块。
3. 实验或效果：在3DTeethSeg基准测试中，高分辨率3D牙齿网格上达到91.90% IoU，创下新最优性能。

## 📄 摘要（原文）

> 3D teeth segmentation, involving the localization of tooth instances and their semantic categorization in 3D dental models, is a critical yet challenging task in digital dentistry due to the complexity of real-world dentition. In this paper, we propose 3DTeethSAM, an adaptation of the Segment Anything Model 2 (SAM2) for 3D teeth segmentation. SAM2 is a pretrained foundation model for image and video segmentation, demonstrating a strong backbone in various downstream scenarios. To adapt SAM2 for 3D teeth data, we render images of 3D teeth models from predefined views, apply SAM2 for 2D segmentation, and reconstruct 3D results using 2D-3D projections. Since SAM2's performance depends on input prompts and its initial outputs often have deficiencies, and given its class-agnostic nature, we introduce three light-weight learnable modules: (1) a prompt embedding generator to derive prompt embeddings from image embeddings for accurate mask decoding, (2) a mask refiner to enhance SAM2's initial segmentation results, and (3) a mask classifier to categorize the generated masks. Additionally, we incorporate Deformable Global Attention Plugins (DGAP) into SAM2's image encoder. The DGAP enhances both the segmentation accuracy and the speed of the training process. Our method has been validated on the 3DTeethSeg benchmark, achieving an IoU of 91.90% on high-resolution 3D teeth meshes, establishing a new state-of-the-art in the field.

