#!/usr/bin/env python3
"""
Test script để kiểm tra logic DES
"""

import main

def test_des():
    print("=== TEST LOGIC DES ===")
    
    # Test case chuẩn từ FIPS 46-3
    M = "0123456789ABCDEF"  # Plaintext
    K = "133457799BBCDFF1"  # Key
    
    print(f"Plaintext M: {M}")
    print(f"Key K: {K}")
    
    # Chuyển sang nhị phân
    M_bits = main.hex_to_bits(M, 64)
    K_bits = main.hex_to_bits(K, 64)
    
    print(f"M (binary): {M_bits}")
    print(f"K (binary): {K_bits}")
    
    # Sinh 16 subkey
    keys, data = main.generate_keys(K_bits)
    print(f"\nSố lượng subkey: {len(keys)}")
    
    # Mã hóa
    C_bits = main.encode(M_bits, keys)
    C_hex = main.bits_to_hex(C_bits).zfill(16)
    print(f"\nBản mã C: {C_hex}")
    
    # Giải mã
    M2_bits = main.decode(C_bits, keys)
    M2_hex = main.bits_to_hex(M2_bits).zfill(16)
    print(f"Giải mã lại M: {M2_hex}")
    
    # Kiểm tra tính đúng đắn
    if M2_hex == M:
        print("✅ TEST PASSED: Giải mã thành công!")
    else:
        print("❌ TEST FAILED: Giải mã không đúng!")
        print(f"Expected: {M}")
        print(f"Got: {M2_hex}")
    
    # Test với dữ liệu khác
    print("\n=== TEST VỚI DỮ LIỆU KHÁC ===")
    M2 = "FEDCBA9876543210"
    K2 = "0E329232EA6D0D73"
    
    print(f"Plaintext M2: {M2}")
    print(f"Key K2: {K2}")
    
    M2_bits = main.hex_to_bits(M2, 64)
    K2_bits = main.hex_to_bits(K2, 64)
    
    keys2, _ = main.generate_keys(K2_bits)
    C2_bits = main.encode(M2_bits, keys2)
    C2_hex = main.bits_to_hex(C2_bits).zfill(16)
    print(f"Bản mã C2: {C2_hex}")
    
    M2_decoded = main.decode(C2_bits, keys2)
    M2_decoded_hex = main.bits_to_hex(M2_decoded).zfill(16)
    print(f"Giải mã lại M2: {M2_decoded_hex}")
    
    if M2_decoded_hex == M2:
        print("✅ TEST PASSED: Giải mã thành công!")
    else:
        print("❌ TEST FAILED: Giải mã không đúng!")

if __name__ == "__main__":
    test_des()

